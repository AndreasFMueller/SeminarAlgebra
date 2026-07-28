%
% sinxx.m -- Stammfunktion von sin(x)/x
%
% (c) 2026 Prof Dr Andreas Müller
%
global range;
range = 10.1;
global a;
a = 1.5;
global N;
N = 1000;

function retval = f(y, x) 
	global a;
	x
	retval = a * sin(pi * x) / x;
end

x = linspace(0.0000001, range, N);
y = lsode(@f, 0, x)

fn = fopen("sinxxdata.tex", "w");
fprintf(fn, "%%\n");
fprintf(fn, "%% sinxxdata.tex -- stammfunktion \n");
fprintf(fn, "%%\n");
fprintf(fn, "%% (c) 2026 Prof Dr Andreas Müller\n");
fprintf(fn, "%%\n");
fprintf(fn, "\\def\\stammfunktion{\n");
fprintf(fn, "\t({%.4f},{%.4f})", x(1), y(1));
for i = (2:N)
	fprintf(fn, "\n\t-- ({%.4f},{%.4f})", x(i), y(i));
end
fprintf(fn, "\n}\n");
fclose(fn);
