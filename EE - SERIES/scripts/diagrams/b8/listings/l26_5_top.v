`timescale 1ns/1ps
// Tang Nano 9K top level: a "breathing" LED from the PWM block and one UART byte per second.
module top (
    input  wire       sys_clk,      // 27 MHz crystal oscillator
    input  wire       btn_n,        // user button (pin 4), active low: used as reset
    output wire       led_n,        // LED, active low
    output wire       uart_tx       // to the on-board USB-UART bridge
);
    wire rst_n = btn_n;

    // Slow ramp for the duty value: changes every 2^17 clocks (4.85 ms), 0..255..0 in 2.5 s.
    reg [24:0] slow;
    reg        down;
    reg [7:0]  duty;
    always @(posedge sys_clk or negedge rst_n) begin
        if (!rst_n) begin
            slow <= 0; duty <= 0; down <= 1'b0;
        end else begin
            slow <= slow + 1'b1;
            if (slow[16:0] == 17'h1FFFF) begin
                if (!down && duty == 8'hFF) down <= 1'b1;
                else if (down && duty == 8'h00) down <= 1'b0;
                else duty <= down ? duty - 1'b1 : duty + 1'b1;
            end
        end
    end

    wire pwm_out;
    pwm #(.WIDTH(8)) u_pwm (.clk(sys_clk), .rst_n(rst_n), .duty(duty), .out(pwm_out));
    assign led_n = ~pwm_out;

    // One byte per second: 27 000 000 clocks.
    reg [24:0] sec;
    reg [7:0]  counter;
    reg        start;
    wire       busy;
    always @(posedge sys_clk or negedge rst_n) begin
        if (!rst_n) begin
            sec <= 0; counter <= 0; start <= 1'b0;
        end else begin
            start <= 1'b0;
            if (sec == 25'd26_999_999) begin
                sec <= 0;
                if (!busy) begin start <= 1'b1; counter <= counter + 1'b1; end
            end else
                sec <= sec + 1'b1;
        end
    end
    uart_tx #(.DIV(234)) u_tx (.clk(sys_clk), .rst_n(rst_n), .data(counter), .start(start),
                               .tx(uart_tx), .busy(busy));
endmodule
