#!/usr/bin/env python3
"""check_listings.py - check every code listing of Book 8 (Firmware and Software for Electronics).

  host C (no SDK)        gcc -std=c11 -Wall -Wextra, compiled and run when the listing has main()
  SDK C / C++ / .ino     gcc/g++ -fsyntax-only against the stub headers in stubs/ (API shapes only)
  Python                 py_compile; runnable listings (no hardware) are also run
  Verilog                iverilog + vvp for the testbenches, verilator --lint-only -Wall
  YAML / CSV / XAML      parsed with pyyaml / csv / xml.etree
  C#                     built and unit-tested with dotnet on Windows (see cscheck/)

Usage: python3 check_listings.py [listings_dir]     Exit code 0 when every check passes.
"""
import csv, os, py_compile, subprocess, sys, tempfile, xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'   # keep the listings folder clean
L = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'listings')
STUBS = os.path.join(HERE, 'stubs')
TMP = tempfile.mkdtemp(prefix='b8chk_')
DEFS = ['-DCONFIG_NODE_WIFI_SSID="lab"', '-DCONFIG_NODE_WIFI_PASSWORD="pw"', '-DCONFIG_NODE_BROKER_URI="mqtt://192.168.1.10"']
SDK_MARKERS = ('"driver/', '"freertos/', '"esp_', '"pico/', '"hardware/', '"stm32', '"soc/', '"mqtt_client', '"nvs_flash')
# Python listings that need hardware, a network, or a camera: compile only.
PY_HW = {'l04_1_bme_id.py', 'l04_2_logger.py', 'l06_3_button_irq.py', 'l07_3_ultrasonic.py', 'l08_1_battery.py',
         'l10_1_oled_spi.py', 'l10_3_can_pc.py', 'l14_3_deepsleep.py', 'l16_1_mpu6050.py', 'l17_2_mqtt_mp.py',
         'l17_4_subscriber.py', 'l18_1_ble_ess.py', 'l20_6_pi_camera.py', 'l21_2_bode.py', 'l23_2_backtrace.py',
         'l24_3_test_hil.py', 'l24_3_conftest.py'}
PY_ARGS = {'l21_1_sweep.py': ['--sim']}
CS_DIR = os.path.join(HERE, 'cscheck')
# Do not require committed/generated obj/project.assets.json files. Each project
# restores its own assets during build so the checker also works from a clean clone.
CS_COMMANDS = {
    'lib': ['dotnet', 'build', os.path.join(CS_DIR, 'lib', 'lib.csproj')],
    'nano': ['dotnet', 'build', os.path.join(CS_DIR, 'nano', 'nano.csproj')],
    'timer': ['dotnet', 'build', os.path.join(CS_DIR, 'timer', 'timer.csproj')],
    'wpf': ['dotnet', 'build', os.path.join(CS_DIR, 'wpf', 'wpf.csproj')],
    'tests': ['dotnet', 'test', os.path.join(CS_DIR, 'tests', 'tests.csproj')],
}
CS_ROUTES = {
    'l05_1_SerialConsole.cs': ('lib',),
    'l05_2_TimerCheck.cs': ('timer',),
    'l05_3_NanoBlink.cs': ('nano',),
    'l22_1_ReadingParser.cs': ('lib', 'tests'),
    'l22_2_ParserTests.cs': ('tests',),
    'l22_3_MainWindow.xaml.cs': ('wpf',),
    'l22_4_TestBench.cs': ('lib', 'tests'),
    'l22_5_BenchTests.cs': ('tests',),
    'l25_4_FirstDraftWindow.cs': ('wpf',),
}
results = []
cs_files = []

def run(cmd, cwd=None, timeout=120):
    try:
        p = subprocess.run(cmd, cwd=cwd or L, capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout + p.stderr).strip()
    except FileNotFoundError:
        return 127, 'tool unavailable: %s' % cmd[0]

def rec(name, how, ok, detail=''):
    if isinstance(detail, str) and detail.startswith('tool unavailable:'):
        ok = None
    results.append((name, how, ok, detail))

for f in sorted(x for x in os.listdir(L) if os.path.isfile(os.path.join(L, x))):
    p = os.path.join(L, f)
    ext = os.path.splitext(f)[1]
    if ext == '.c':
        src = open(p).read()
        if any(m in src for m in SDK_MARKERS):
            rc, out = run(['gcc', '-std=gnu11', '-Wall', '-fsyntax-only', '-I' + STUBS] + DEFS + [f])
            rec(f, 'gcc -fsyntax-only (SDK stubs)', rc == 0 and 'warning' not in out, out)
        elif f == 'l24_2_test_ringbuf.c':
            exe = os.path.join(TMP, 'ringtest')
            rc, out = run(['gcc', '-std=c11', '-Wall', '-Wextra', '-o', exe, f, 'l24_1_ringbuf.c'])
            if rc == 0:
                rc, out = run([exe])
            rec(f, 'gcc + run with l24_1_ringbuf.c', rc == 0 and '0 failures' in out, out.splitlines()[-1] if out else '')
        elif 'RCC_AHB1ENR' in src:          # bare-metal STM32 code: compile only, never run on the host
            rc, out = run(['gcc', '-std=c11', '-Wall', '-Wextra', '-fsyntax-only', f])
            rec(f, 'gcc -Wall -Wextra -fsyntax-only (bare metal)', rc == 0 and 'warning' not in out, out)
        elif 'main(' in src:
            exe = os.path.join(TMP, f[:-2])
            rc, out = run(['gcc', '-std=c11', '-Wall', '-Wextra', '-o', exe, f, '-lm'])
            ok = rc == 0 and 'warning' not in out
            if ok:
                rc, out = run([exe]); ok = rc == 0
            rec(f, 'gcc -Wall -Wextra + run', ok, out.splitlines()[0] if out else '')
        else:
            rc, out = run(['gcc', '-std=c11', '-Wall', '-Wextra', '-fsyntax-only', f])
            rec(f, 'gcc -fsyntax-only', rc == 0 and 'warning' not in out, out)
    elif ext == '.h':
        rc, out = run(['gcc', '-std=c11', '-Wall', '-fsyntax-only', f])
        rec(f, 'gcc -fsyntax-only', rc == 0, out)
    elif ext in ('.cpp', '.ino'):
        extra = ['-include', 'Arduino.h'] if ext == '.ino' else []
        rc, out = run(['g++', '-std=gnu++17', '-Wall', '-fsyntax-only', '-I' + STUBS] + extra + ['-x', 'c++', f])
        rec(f, 'g++ -fsyntax-only (Arduino stubs)', rc == 0 and 'warning' not in out, out)
    elif ext == '.py':
        try:
            py_compile.compile(p, cfile=os.path.join(TMP, f + 'c'), doraise=True); ok, out = True, ''
        except py_compile.PyCompileError as e:
            ok, out = False, str(e)
        if ok and f not in PY_HW:
            args = PY_ARGS.get(f, [])
            if f == 'l19_3_manifest.py':
                fw = os.path.join(TMP, 'firmware.bin'); open(fw, 'wb').write(bytes(range(256)) * 64); args = [fw, '1.4.2']
            rc, out = run([sys.executable, p] + args, cwd=TMP, timeout=300)
            ok = rc == 0
            rec(f, 'py_compile + run', ok, out.splitlines()[-1] if out else '')
        else:
            rec(f, 'py_compile (needs hardware)' if ok else 'py_compile', ok, out)
    elif ext == '.v' and f.endswith('_tb.v'):
        dut = {'l26_2_pwm_tb.v': 'l26_1_pwm.v', 'l26_4_uart_tb.v': 'l26_3_uart_tx.v'}[f]
        vvp = os.path.join(TMP, f + '.vvp')
        rc, out = run(['iverilog', '-g2012', '-Wall', '-o', vvp, f, dut])
        if rc == 0:
            rc, out = run(['vvp', '-n', vvp], cwd=TMP)
        ok = rc == 0 and any(l.strip() == '0 errors' for l in out.splitlines()) and 'FAIL' not in out
        detail = [l for l in out.splitlines() if 'errors' in l][-1:] if rc == 0 else out
        rec(f, 'iverilog + vvp (with %s)' % dut, ok, detail)
    elif ext == '.v':
        files = [f] if f != 'l26_5_top.v' else [f, 'l26_1_pwm.v', 'l26_3_uart_tx.v']
        rc, out = run(['verilator', '--lint-only', '-Wall', '-Wno-DECLFILENAME', '--top-module',
                       {'l26_1_pwm.v': 'pwm', 'l26_3_uart_tx.v': 'uart_tx', 'l26_5_top.v': 'top'}[f]] + files)
        rec(f, 'verilator --lint-only -Wall', rc == 0, out)
    elif ext == '.yml':
        try:
            import yaml
            d = yaml.safe_load(open(p)); ok, out = isinstance(d, dict) and 'jobs' in d, ''
        except ImportError:
            ok, out = None, 'tool unavailable: PyYAML'
        except Exception as e:
            ok, out = False, str(e)
        rec(f, 'yaml.safe_load (jobs present)', ok, out)
    elif ext == '.csv':
        rows = [r for r in csv.reader(l for l in open(p) if l.strip() and not l.startswith('#'))]
        rec(f, 'csv parse (5 columns per row)', all(len(r) >= 5 for r in rows), '%d rows' % len(rows))
    elif ext == '.xaml':
        try:
            ET.parse(p); ok, out = True, ''
        except ET.ParseError as e:
            ok, out = False, str(e)
        rec(f, 'XML well-formed', ok, out)
    elif ext == '.cs':
        cs_files.append(f)
    elif ext in ('.cst', '.ini', '.txt'):
        rec(f, 'text (not compiled)', None, '')
    else:
        rec(f, 'unknown type', False, '')

if cs_files:
    cs_results = {}
    for project, cmd in CS_COMMANDS.items():
        rc, out = run(cmd, cwd=HERE, timeout=300)
        available = not out.startswith('tool unavailable:')
        cs_results[project] = (available, rc == 0, out)
    for f in cs_files:
        route = CS_ROUTES.get(f)
        if route is None:
            rec(f, 'dotnet route missing', False, 'Add this listing to CS_ROUTES and cscheck/ before relying on project results.')
            continue
        statuses = [cs_results[name] for name in route]
        if any(not available for available, _, _ in statuses):
            rec(f, 'dotnet ' + '+'.join(route) + ' (cscheck/)', None, 'tool unavailable: dotnet')
        else:
            ok = all(passed for _, passed, _ in statuses)
            details = [out.splitlines()[-1] for _, _, out in statuses if out.strip()]
            rec(f, 'dotnet ' + '+'.join(route) + ' (cscheck/)', ok, '; '.join(details))

w = max(len(r[0]) for r in results)
fails = 0
for name, how, ok, detail in results:
    tag = 'ok  ' if ok else ('n/a ' if ok is None else 'FAIL')
    fails += ok is False
    print('%s %-*s %s' % (tag, w, name, how) + ('   | %s' % detail if (detail and ok is not None and not ok) else ''))
print('\n%d listings, %d checked ok, %d not checkable here, %d failed' %
      (len(results), sum(r[2] is True for r in results), sum(r[2] is None for r in results), fails))
sys.exit(1 if fails else 0)
