import time
import tracemalloc

class TestCase():
    def test_case(self, *args):
        # Thiết lập độ rộng cột
        w_stt, w_status, w_time, w_mem = 5, 10, 12, 12
        w_act, w_exp = 20, 20
        
        # In tiêu đề bảng
        header = (f"{'STT':<{w_stt}} | {'Status':<{w_status}} | "
                  f"{'Time (ms)':<{w_time}} | {'Mem (KB)':<{w_mem}} | "
                  f"{'Actual':<{w_act}} | {'Expected':<{w_exp}}")
        print(header)
        print("-" * len(header))

        test_cases = []
        if len(args) == 2:
            test_cases = [(args[0], args[1])]
        elif len(args) == 1:
            inputs = args[0]
            if isinstance(inputs, (list, tuple)) and len(inputs) == 2 and \
               not (isinstance(inputs[0], (list, tuple)) and len(inputs[0]) == 2):
                test_cases = [(inputs[0], inputs[1])]
            elif isinstance(inputs, (list, tuple)):
                for item in inputs:
                    if isinstance(item, (list, tuple)) and len(item) == 2:
                        test_cases.append((item[0], item[1]))
                    else:
                        test_cases.append((item, "Missing Expected"))
            else:
                test_cases = [(inputs, "Missing Expected")]
        
        for count, (item, expected) in enumerate(test_cases):
            # Bắt đầu đo tài nguyên và thời gian
            tracemalloc.start()
            start_time = time.perf_counter()
            
            # Thực thi nếu item là callable, nếu không coi như kết quả đã có sẵn
            if callable(item):
                try:
                    actual = item()
                except Exception as e:
                    actual = f"Error: {e}"
            else:
                actual = item
            
            # Kết thúc đo
            end_time = time.perf_counter()
            _, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            duration_ms = (end_time - start_time) * 1000
            mem_kb = peak / 1024
            
            status = "PASS" if actual == expected else "FAIL"

            def format_val(val, width):
                s = str(val)
                return (s[:width-3] + "...") if len(s) > width else s

            act_str = format_val(actual, w_act)
            exp_str = format_val(expected, w_exp)

            print(f"{count + 1:<{w_stt}} | "
                  f"{status:<{w_status}} | "
                  f"{duration_ms:<{w_time}.4f} | "
                  f"{mem_kb:<{w_mem}.2f} | "
                  f"{act_str:<{w_act}} | "
                  f"{exp_str:<{w_exp}}")
