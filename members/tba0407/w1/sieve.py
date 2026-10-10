"""
    Tìm các số nguyên tố từ 2 đến n bằng thuật toán Sàng Eratosthenes.

    Khác biệt xử lý giữa Python và C++:
    - Khởi tạo mảng: Python khởi tạo nhanh bằng `[True] * (n + 1)`, C++ cần dùng mảng tĩnh hoặc `std::vector<bool>`.
    - Thêm phần tử: Python dùng `.append()` tự động cấp phát bộ nhớ, C++ cần dùng `push_back()` hoặc cấp phát kích thước trước.
    - Hiệu suất: Python viết nhanh, dễ đọc nhưng chạy chậm và tốn RAM. C++ kiểm soát bộ nhớ chặt chẽ nên tối ưu và chạy nhanh hơn.
"""

def sieve(n: int) -> list[int]:
    if n < 2: return []

    isPrime = [True]*(n + 1)

    isPrime[0] = isPrime[1] = False

    for i in range(4, n + 1, 2):
        isPrime[i] = False

    p = 3
    while p * p <= n:
        if not isPrime[p]: continue

        for i in range(p * p, n + 1, 2 * p):
            isPrime[i] = False

        p += 2


    primes = []
    for i in range(2, n + 1):
        if not isPrime[i]: continue

        primes.append(i)

    return primes