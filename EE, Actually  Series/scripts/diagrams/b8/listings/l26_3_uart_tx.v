`timescale 1ns/1ps
// UART transmitter, 8N1. DIV = clock / baud, rounded: 27 MHz / 115200 = 234.375 -> 234.
module uart_tx #(
    parameter DIV = 234
) (
    input  wire       clk,
    input  wire       rst_n,
    input  wire [7:0] data,
    input  wire       start,      // one-clock pulse; ignored while busy
    output reg        tx,         // idles high
    output wire       busy
);
    reg [15:0] tick;              // clocks within the current bit
    reg [3:0]  bit_idx;           // 0 = start bit, 1..8 = data, 9 = stop bit
    reg [9:0]  frame;
    reg        active;

    assign busy = active;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            tx <= 1'b1; active <= 1'b0; tick <= 0; bit_idx <= 0; frame <= 10'h3FF;
        end else if (!active) begin
            tx <= 1'b1;
            if (start) begin
                frame   <= {1'b1, data, 1'b0};   // stop, data (LSB first), start
                active  <= 1'b1;
                tick    <= 0;
                bit_idx <= 0;
                tx      <= 1'b0;                  // start bit begins now
            end
        end else if (tick == DIV - 1) begin
            tick <= 0;
            if (bit_idx == 9) begin
                active <= 1'b0;                   // stop bit done
                tx     <= 1'b1;
            end else begin
                bit_idx <= bit_idx + 1'b1;
                tx      <= frame[bit_idx + 1];
            end
        end else begin
            tick <= tick + 1'b1;
        end
    end
endmodule
