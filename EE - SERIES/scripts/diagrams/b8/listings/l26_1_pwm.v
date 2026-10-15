`timescale 1ns/1ps
// 8-bit PWM: the output is high while the free-running counter is below the duty value.
// At 27 MHz (Tang Nano 9K) the period is 256 clocks = 9.48 us, i.e. 105.5 kHz.
module pwm #(
    parameter WIDTH = 8
) (
    input  wire             clk,
    input  wire             rst_n,     // active-low reset
    input  wire [WIDTH-1:0] duty,      // 0 = always off, 255 = on for 255 of 256 clocks
    output reg              out
);
    reg [WIDTH-1:0] count;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            count <= {WIDTH{1'b0}};
            out   <= 1'b0;
        end else begin
            count <= count + 1'b1;               // wraps from 255 to 0
            out   <= (count < duty);             // registered output: no glitches
        end
    end
endmodule
