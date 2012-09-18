program triangle;

{$mode tp}{$H+}

var
  x1,x2,x3,y1,y2,y3 : integer;
  perimeter:          real;
  l1, l2, l3: real;
begin
  WriteLn('Data format: <X> <RET> <Y>');
  WriteLn('Enter first point coordinates:');
  Read(x1,y1);
  WriteLn('Enter second point coordinates:');
  Read(x2,y2);
  WriteLn('Enter third point coordinates:');
  Read(x3,y3);
  l1 := sqrt(sqr(x1-x2) + sqr(y1-y2));
  l2 := sqrt(sqr(x1-x3) + sqr(y1-y3));
  l3 := sqrt(sqr(x2-x3) + sqr(y2-y3));
  perimeter := l1 + l2 + l3;
  WriteLn('Perimeter: ', perimeter);
end.

