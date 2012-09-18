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
  WriteLn('Введите основание равнобедренной трапеции №1');
  Read(base2);
  WriteLn('Введите основание равнобедренной трапеции №2');
  Read(base2);
  WriteLn('Введите высоту равнобедренной трапеции');
  Read(header);
  (* Вычисляю длину боковой стороны, отсекая из большей стороны меньшую,
  деля на 2 и применяя т. Пифагора *)
  trapezoid := abs(base1-base2)/2;
  trapezoid := sqrt(sqr(header) + sqr(trapezoid));

  perimeter := 2*trapezoid + base1 + base2;
  area := (base1 + base2)/2*header;
  WriteLn ('Периметр трапеции: ', perimeter:4:4, '; площадь трапеции: ', area:4:4);
end.


