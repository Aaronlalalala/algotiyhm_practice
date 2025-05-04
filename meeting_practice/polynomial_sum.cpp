#include "polynomial_sum.h"
#include "stdio.h"

int calculation_polynomail_sum(int N) {
	int sum = 0;
	for (int i = 0; i < N; i++) {
		if (i % 2 == 0) {
			sum -= i;
		}
		else {
			sum += i;
		}
	}
	return sum;
}