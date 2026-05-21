package main

import (
	"fmt"
	"runtime"
	"strings"
	"time"
)

// TestData represents a single test case
type TestData struct {
	Actual   interface{}
	Expected interface{}
	Run      func() interface{} // Optional: function to execute
}

// TestCase handles running and reporting test results
type TestCase struct{}

func (tc *TestCase) Run(tests []TestData) {
	// Column widths
	wStt, wStatus, wTime, wMem := 5, 10, 12, 12
	wAct, wExp := 20, 20

	// Header
	header := fmt.Sprintf("%-*s | %-*s | %-*s | %-*s | %-*s | %-*s",
		wStt, "STT", wStatus, "Status", wTime, "Time (ms)", wMem, "Mem (KB)", wAct, "Actual", wExp, "Expected")
	fmt.Println(header)
	fmt.Println(strings.Repeat("-", len(header)))

	for i, test := range tests {
		var memStart, memEnd runtime.MemStats
		runtime.GC() // Clean up before measurement
		runtime.ReadMemStats(&memStart)
		startTime := time.Now()

		var actual interface{}
		if test.Run != nil {
			actual = test.Run()
		} else {
			actual = test.Actual
		}

		duration := time.Since(startTime)
		runtime.ReadMemStats(&memEnd)

		// Calculate peak memory (approximation in Go)
		memKB := float64(memEnd.TotalAlloc-memStart.TotalAlloc) / 1024
		if memKB < 0 {
			memKB = 0
		}

		status := "FAIL"
		if fmt.Sprintf("%v", actual) == fmt.Sprintf("%v", test.Expected) {
			status = "PASS"
		}

		formatVal := func(val interface{}, width int) string {
			s := fmt.Sprintf("%v", val)
			if len(s) > width {
				return s[:width-3] + "..."
			}
			return s
		}

		fmt.Printf("%-*d | %-*s | %-*.4f | %-*.2f | %-*s | %-*s\n",
			wStt, i+1, wStatus, status, wTime, float64(duration.Microseconds())/1000.0,
			wMem, memKB, wAct, formatVal(actual, wAct), wExp, formatVal(test.Expected, wExp))
	}
}

func main() {
	tc := &TestCase{}

	// Example usage
	tests := []TestData{
		{
			Expected: 5,
			Run: func() interface{} {
				time.Sleep(10 * time.Millisecond)
				return 2 + 3
			},
		},
		{
			Actual:   "hello",
			Expected: "world",
		},
	}

	tc.Run(tests)
}
