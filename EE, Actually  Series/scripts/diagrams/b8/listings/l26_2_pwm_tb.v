// Testbench: measure the PWM duty cycle over whole periods and compare with the setting.
`timescale 1ns/1ps
module pwm_tb;
    reg clk = 0, rst_n = 0;
    reg [7:0] duty;
    wire out;
    integer high, i, errors = 0;

    pwm #(.WIDTH(8)) dut (.clk(clk), .rst_n(rst_n), .duty(duty), .out(out));
    always #18.518 clk = ~clk;                   // 27 MHz: period 37.037 ns

    task check(input [7:0] d);
        begin
            duty = d;
            repeat (256) @(posedge clk);         // let the new value take effect
            high = 0;
            for (i = 0; i < 256; i = i + 1) begin
                @(posedge clk);
                high = high + out;
            end
            if (high !== d) begin
                errors = errors + 1;
                $display("FAIL duty %0d: %0d of 256 clocks high", d, high);
            end else
                $display("ok   duty %3d: %3d of 256 clocks high (%.1f %%)", d, high, 100.0 * high / 256);
        end
    endtask

    initial begin
        $dumpfile("pwm.vcd");
        $dumpvars(0, pwm_tb);
        duty = 0;
        #100 rst_n = 1;
        check(0); check(1); check(64); check(128); check(255);
        $display("%0d errors", errors);
        $finish;
    end
endmodule
