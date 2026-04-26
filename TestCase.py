class TestCase():
    def test_case(self, *args):
        # Thiết lập độ rộng cột
        w_stt, w_status, w_act, w_exp = 5, 10, 25, 25
        
        # In tiêu đề bảng
        header = f"{'STT':<{w_stt}} | {'Status':<{w_status}} | {'Actual':<{w_act}} | {'Expected':<{w_exp}}"
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
        
        for count, (actual, expected) in enumerate(test_cases):
            status = "PASS" if actual == expected else "FAIL"

            def format_val(val, width):
                s = str(val)
                return (s[:width-3] + "...") if len(s) > width else s

            act_str = format_val(actual, w_act)
            exp_str = format_val(expected, w_exp)

            print(f"{count + 1:<{w_stt}} | {status:<{w_status}} | {act_str:<{w_act}} | {exp_str:<{w_exp}}")
