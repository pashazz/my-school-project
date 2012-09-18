program trapeze;

{$mode tp}{$H+}

uses
  crt;
var header: real;
    base1, base2: real;
    perimeter: real;
    trapezoid: real;
    area:      real;
begin
  WriteLn('Trapeze base #1:');
  Read(base1);
  WriteLn('Trapeze base #2:');
  Read(base2);
  WriteLn('Trapeze header:');
  Read(header);
  (* Вычисляю длину боковой стороны, отсекая из большей стороны меньшую,
  деля на 2 и применяя т. Пифагора *)
  trapezoid := abs(base1-base2)/2;
  trapezoid := sqrt(sqr(header) + sqr(trapezoid));

  perimeter := 2*trapezoid + base1 + base2;
  area := (base1 + base2)/2*header;
  WriteLn ('P: ', perimeter:4:4, '; S: ', area:4:4);
end.


