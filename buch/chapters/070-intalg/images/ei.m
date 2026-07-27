%
% ei.m -- generate curves for exponential integral
%
% (c) 2026 Prof Dr Andreas Müller
%
N = 200;

function kurve(fn, name, x, y)
	n = size(x)(2);
	fprintf(fn, "\\def\\kurve%s{\n", name);
	fprintf(fn, "\t({%.4f*\\dx},{%.4f*\\dy})", x(1), y(1));
	for i = (2:n)
		fprintf(fn, "\n\t--({%.4f*\\dx},{%.4f*\\dy})", x(i), y(i));
	end
	fprintf(fn, "\n}\n");
end

fn = fopen("eipaths.tex", "w");

x = linspace(0.001,3.1,N);
y = -arrayfun(@expint, -x) - pi*1i
kurve(fn, "links", x, y);

x = linspace(-0.001,-3.1,N);
y = -arrayfun(@expint, -x)
kurve(fn, "rechts", x, y);

fclose(fn);
