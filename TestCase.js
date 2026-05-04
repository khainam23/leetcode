const { performance } = require('perf_hooks');

class TestCase {
    /**
     * Chạy các test case và in kết quả ra bảng.
     * @param  {...any} args - Có thể là (actual, expected) hoặc một mảng các test case.
     */
    test_case(...args) {
        // Thiết lập độ rộng cột
        const w_stt = 5, w_status = 10, w_time = 12, w_mem = 12;
        const w_act = 20, w_exp = 20;

        // In tiêu đề bảng
        const header = `${'STT'.padEnd(w_stt)} | ${'Status'.padEnd(w_status)} | ` +
                       `${'Time (ms)'.padEnd(w_time)} | ${'Mem (KB)'.padEnd(w_mem)} | ` +
                       `${'Actual'.padEnd(w_act)} | ${'Expected'.padEnd(w_exp)}`;
        console.log(header);
        console.log("-".repeat(header.length));

        let test_cases = [];
        if (args.length === 2) {
            test_cases = [[args[0], args[1]]];
        } else if (args.length === 1) {
            const inputs = args[0];
            // Kiểm tra nếu là [actual, expected] thay vì mảng các test case
            if (Array.isArray(inputs) && inputs.length === 2 &&
                !(Array.isArray(inputs[0]) && inputs[0].length === 2)) {
                test_cases = [[inputs[0], inputs[1]]];
            } else if (Array.isArray(inputs)) {
                for (const item of inputs) {
                    if (Array.isArray(item) && item.length === 2) {
                        test_cases.push([item[0], item[1]]);
                    } else {
                        test_cases.push([item, "Missing Expected"]);
                    }
                }
            } else {
                test_cases = [[inputs, "Missing Expected"]];
            }
        }

        test_cases.forEach((test, index) => {
            const [item, expected] = test;
            
            // Đo bộ nhớ ban đầu
            const startMem = process.memoryUsage().heapUsed;
            const startTime = performance.now();

            let actual;
            if (typeof item === 'function') {
                try {
                    actual = item();
                } catch (e) {
                    actual = `Error: ${e.message}`;
                }
            } else {
                actual = item;
            }

            const endTime = performance.now();
            const endMem = process.memoryUsage().heapUsed;

            const duration_ms = endTime - startTime;
            // Mem (KB) trong JS chỉ mang tính chất tham khảo do cơ chế GC
            const mem_kb = Math.max(0, (endMem - startMem) / 1024);
            
            // So sánh giá trị (sử dụng JSON.stringify để so sánh mảng/object đơn giản)
            const status = JSON.stringify(actual) === JSON.stringify(expected) ? "PASS" : "FAIL";

            const formatVal = (val, width) => {
                let s = (typeof val === 'object' && val !== null) ? JSON.stringify(val) : String(val);
                return s.length > width ? s.substring(0, width - 3) + "..." : s;
            };

            const act_str = formatVal(actual, w_act);
            const exp_str = formatVal(expected, w_exp);

            console.log(
                `${(index + 1).toString().padEnd(w_stt)} | ` +
                `${status.padEnd(w_status)} | ` +
                `${duration_ms.toFixed(4).padEnd(w_time)} | ` +
                `${mem_kb.toFixed(2).padEnd(w_mem)} | ` +
                `${act_str.padEnd(w_act)} | ` +
                `${exp_str.padEnd(w_exp)}`
            );
        });
    }
}

module.exports = TestCase;
