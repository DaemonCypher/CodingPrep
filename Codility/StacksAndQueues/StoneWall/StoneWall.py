def solution(H):
    stack = []
    block_count = 0

    for height in H:
        # Remove all blocks that are higher than the current height
        while stack and stack[-1] > height:
            stack.pop()

        # If the stack is empty or the current height is higher than the top of the stack,
        # a new block is needed
        if not stack or stack[-1] < height:
            block_count += 1
            stack.append(height)

    return block_count
# Chatgpt
# 100%