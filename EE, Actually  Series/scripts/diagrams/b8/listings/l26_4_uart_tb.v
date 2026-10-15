// Testbench: a behavioral receiver samples tx in the middle of each bit and checks the bytes.
`timescale 1ns/1ps
module uart_tb;
    localparam DIV = 234;
    reg clk = 0, rst_n = 0, start = 0;
    reg [7:0] data;
    wire tx, busy;
    integer errors = 0, k;
    reg [7:0] got;
    reg [7:0] tests [0:3];
    real t0, t1;

    uart_tx #(.DIV(DIV)) dut (.clk(clk), .rst_n(rst_n), .data(data), .start(start), .tx(tx), .busy(busy));
    always #18.518 clk = ~clk;                   // 27 MHz

    task receive(output [7:0] b);
        integer n;
        begin
            @(negedge tx);                          // start bit edge
            t0 = $realtime;
            repeat (DIV / 2) @(posedge clk);        // middle of the start bit
            if (tx !== 1'b0) $display("FAIL: start bit not low");
            for (n = 0; n < 8; n = n + 1) begin
                repeat (DIV) @(posedge clk);
                b[n] = tx;                          // LSB first
            end
            repeat (DIV) @(posedge clk);
            if (tx !== 1'b1) begin errors = errors + 1; $display("FAIL: stop bit not high"); end
            t1 = $realtime;
        end
    endtask

    initial begin
        tests[0] = 8'h55; tests[1] = 8'hA3; tests[2] = 8'h00; tests[3] = 8'hFF;
        $dumpfile("uart.vcd");
        $dumpvars(0, uart_tb);
        #100 rst_n = 1;
        for (k = 0; k < 4; k = k + 1) begin
            fork
                receive(got);                          // listening before the start bit
                begin
                    @(negedge clk) begin data = tests[k]; start = 1; end   // away from the DUT's edge
                    @(negedge clk) start = 0;
                end
            join
            if (got !== tests[k]) begin
                errors = errors + 1;
                $display("FAIL sent %h got %h", tests[k], got);
            end else
                $display("ok   sent %h got %h", tests[k], got);
            wait (!busy);
        end
        $display("bit time %.1f ns -> %.0f baud", (t1 - t0) / 9.5, 9.5e9 / (t1 - t0));
        $display("%0d errors", errors);
        $finish;
    end
endmodule
