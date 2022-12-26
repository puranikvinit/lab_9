`timescale 1ns/1ns
`include "accumulator.v"

module accumulator_tb();
    reg [7:0] in;
    reg clk, reset;
    wire [7:0] acc;

    accumulator AC(in, acc, clk, reset);

    initial begin
        $dumpfile("accumulator.vcd");
        $dumpvars();
    end

    always
        #5 clk = ~clk;

    initial begin
        clk = 0;

        #5 reset = 1'b1;

        #5 reset = 1'b0;
        in = 8'b00000001; #50; in = 8'b00000010; #50; in = 8'b00000011;
    end

    initial begin
        $display("Test Completed!!");
        #200 $finish;
    end
endmodule