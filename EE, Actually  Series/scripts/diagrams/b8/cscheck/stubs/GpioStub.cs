// Compile-check stub for nanoFramework System.Device.Gpio (package not in the offline cache).
namespace System.Device.Gpio
{
    public enum PinMode { Input, Output, InputPullDown, InputPullUp }
    public enum PinValue { Low = 0, High = 1 }
    public class GpioPin { public void Toggle() { } public void Write(PinValue v) { } public PinValue Read() => PinValue.Low; }
    public class GpioController { public GpioPin OpenPin(int pin, PinMode mode) => new GpioPin(); }
}
