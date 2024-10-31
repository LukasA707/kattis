package main

import (
	"fmt"
)

func main() {
	var input int
	fmt.Scan(&input)
	fmt.Printf("%d", calc(input))
}

func calc(n int) int {
	if n <= 4 {
		return 4
	}
	return n + calc(n/4)
}
