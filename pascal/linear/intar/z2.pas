program z2;
	uses crt;
var
	day,wday: Integer;

begin
	clrscr;
	writeln('Enter the day of year');
	read(day);
	wday := day div 7 - (day mod 7);
	writeln ('the day of week is:', wday);

readkey;
end.
