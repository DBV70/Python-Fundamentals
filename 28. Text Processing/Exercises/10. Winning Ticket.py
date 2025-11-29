def is_valid(ticket:str) -> str:
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ('@', '#', '$', '^')
    left_part = ticket[:10]
    right_part = ticket[10:]
    for current_winning_symbol in winning_symbols:
        for i in range(10, 5, -1):
            winning_symbol_count = current_winning_symbol * i
            if winning_symbol_count in left_part and winning_symbol_count in right_part:
                if i == 10:
                    return f'ticket "{ticket}" - {i}{current_winning_symbol} Jackpot!'
                return f'ticket "{ticket}" - {i}{current_winning_symbol}'

    return f'ticket "{ticket}" - no match'

tickets = [ticket.strip() for ticket in input().split(", ")]
for current_ticket in tickets:
    print(is_valid(current_ticket))