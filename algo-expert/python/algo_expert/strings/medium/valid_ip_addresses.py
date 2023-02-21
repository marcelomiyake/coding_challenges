def valid_ip_addresses(string: str) -> list:
    result = []
    for p1 in range(1, 4):
        for p2 in range(1, 4):
            for p3 in range(1, 4):
                for p4 in range(1, 4):
                    if p1 + p2 + p3 + p4 == len(string):
                        octet1 = string[:p1]
                        octet2 = string[p1:p1 + p2]
                        octet3 = string[p1 + p2:p1 + p2 + p3]
                        octet4 = string[p1 + p2 + p3:]
                        if is_valid(octet1) and is_valid(octet2) and is_valid(octet3) and is_valid(octet4):
                            result.append(".".join([octet1, octet2, octet3, octet4]))
    return result


def is_valid(octet: str) -> bool:
    return int(octet) < 256 and not (len(octet) > 1 and octet[0] == "0")
