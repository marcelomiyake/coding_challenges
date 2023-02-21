from algo_expert.strings.medium.valid_ip_addresses import valid_ip_addresses


class TestValidIPAddresses:
    def test_case_0(self):
        string = "1921680"

        expected = [
            "1.9.216.80",
            "1.92.16.80",
            "1.92.168.0",
            "19.2.16.80",
            "19.2.168.0",
            "19.21.6.80",
            "19.21.68.0",
            "19.216.8.0",
            "192.1.6.80",
            "192.1.68.0",
            "192.16.8.0"
        ]

        assert sorted(valid_ip_addresses(string)) == sorted(expected)
