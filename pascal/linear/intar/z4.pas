program z4;
	uses crt;
var
	a,b,c,k,l,m, c1,c2,c3, res: Integer;
begin
	clrscr;
	writeln('Enter a,b,c, k, l, m');
	read(a,b,c,k,l,m);
	c1 := k mod a;
	c2 := b mod l;
	c3 := c mod m;
	res := (c1*c2*c3) div (k*l*m);
	writeln(res);



readkey;
end.
