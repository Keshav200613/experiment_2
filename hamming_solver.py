from itertools import product
from typing import List, Dict, Tuple, Optional

def parse_codeword(codeword: str) -> Tuple[List[Optional[int]], Dict[int, str]]:
    bits: List[Optional[int]] = []
    unknowns: Dict[int, str] = {}
    for idx, char in enumerate(codeword):
        if char in ('0', '1'):
            bits.append(int(char))
        else:
            bits.append(None)
            unknowns[idx] = char
    return bits, unknowns


def is_hamming_valid(bits: List[Optional[int]], check_positions: List[int]) -> bool:
    n = len(bits)
    for pos in check_positions:
        idx = pos - 1
        parity = 0
        i = idx
        step = (idx + 1) * 2
        while i < n:
            segment = bits[i:i + idx + 1]
            if None in segment:
                return False
            parity ^= sum(segment) % 2
            i += step
        if parity != 0:
            return False
    return True


def solve_hamming_code(codeword: str, check_positions: List[int]) -> Tuple[Optional[Dict[str, int]], Optional[str]]:
    bits, unknowns = parse_codeword(codeword)
    unknown_indices = list(unknowns.keys())
    from itertools import product
    for candidate in product([0, 1], repeat=len(unknown_indices)):
        test_bits = bits[:]
        for idx, bit in zip(unknown_indices, candidate):
            test_bits[idx] = bit
        if is_hamming_valid(test_bits, check_positions):
            solution: Dict[str, int] = {unknowns[idx]: bit for idx, bit in zip(unknown_indices, candidate)}
            completed = ''.join(str(b) for b in test_bits)
            return solution, completed
    return None, None


def main():
    print("Alternate Hamming Code Solver")
    codeword = input("Enter codeword (use x/y/_ for unknowns): ").strip()
    check_str = input("Check bit positions (comma separated, e.g. 1,2,4,8): ").strip()
    try:
        check_positions = [int(x) for x in check_str.split(',')]
    except ValueError:
        print("Invalid check bit positions. Please enter comma-separated integers.")
        return
    solution, completed = solve_hamming_code(codeword, check_positions)
    if solution:
        print("Solution:")
        for placeholder, value in solution.items():
            print(f"{placeholder} = {value}")
        print(f"Filled codeword: {completed}")
    else:
        print("No valid solution found.")


if __name__ == "__main__":
    main()
