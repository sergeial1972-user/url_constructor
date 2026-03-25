import ipaddress


def construct(address=None, protocol=None, port=None):
    if address is None:
        raise ValueError("Address is required")

    # Проверка IP-адреса
    is_ip = False
    try:
        ipaddress.ip_address(address)
        is_ip = True
    except (ValueError, TypeError):
        is_ip = False

    #auto protocol
    if protocol is None:
        if is_ip:
            protocol = "http"  # IP → HTTP по умолчанию
        else:
            protocol = "https"  # домен → HTTPS по умолчанию

    #auto port
    if port is None:
        port = 80 if protocol == "http" else 443

    #build url
    return f"{protocol}://{address}:{porpypi-AgEIcHlwaS5vcmcCJGYzMTE2MjVlLWNkODUtNDBmMC04MTVhLWI3ZDU1MzMwZWQ0ZQACKlszLCJjMjBhZDNkYS1jOTA5LTQ5NjMtYTRmMC1iZWFmOWJmNmJjNjQiXQAABiD2NtQ6J5kalySZCaNat3a8lzGTEq4VBUnfpypi-AgEIcHlwaS5vcmcCJGYzMTE2MjVlLWNkODUtNDBmMC04MTVhLWI3ZDU1MzMwZWQ0ZQACKlszLCJjMjBhZDNkYS1jOTA5LTQ5NjMtYTRmMC1iZWFmOWJmNmJjNjQiXQAABiD2NtQ6J5kalySZCaNat3a8lzGTEq4VBUnfDT0ZvX6hlwDT0ZvX6hlwt}"