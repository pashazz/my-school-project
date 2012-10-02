program z1;
	uses crt;
var
	s_circle,s_square,diameter,a,h: real;
begin
	writeln('Enter circle and square domain:');
	read(s_circle,s_square);
	diameter := s_circle/pi;
	a := sqrt(s_square);
	if diameter <= a then writeln('circle in the square')
	else
		begin
			h := sqrt(2*a*a);
			if diameter >= h then writeln('square in the circle')
			else writeln('Neither square in the circle nor circle in the square');
		end;

end.
