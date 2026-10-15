// .NET nanoFramework on an ESP32-S3: blink an LED on GPIO 4 in C#.
// Project: Visual Studio with the nanoFramework extension; NuGet nanoFramework.System.Device.Gpio
using System.Device.Gpio;
using System.Threading;

namespace NanoBlink
{
    public class Program
    {
        public static void Main()
        {
            var gpio = new GpioController();
            GpioPin led = gpio.OpenPin(4, PinMode.Output);
            while (true)
            {
                led.Toggle();
                Thread.Sleep(500);
            }
        }
    }
}
