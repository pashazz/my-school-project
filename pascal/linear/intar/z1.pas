program  z1;
	uses crt;
var
	x,a1,a2,a3,a4:Integer;
begin
	clrscr;
	writeln('Enter 4digit X');
	read(x);
	a1 := x div 1000;
	a2 := x mod 1000 div 100;
	a3 := x mod 100 div 10;
	a4 := x mod 10 div 1; 
	(* writeln(a1,';',a2,';',a3,';',a4); *)
	writeln ('Sum of digits: ', a1+a2+a3+a4); 
end.
