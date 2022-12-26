module accumulator(in, acc, clk, reset);
    input [7:0] in;
    input clk, reset;

    output reg [7:0] acc;

    always@(posedge clk, reset)
    begin
        if(reset) acc <= 8'b00000000;
        else acc <= acc + in;
    end
endmodule