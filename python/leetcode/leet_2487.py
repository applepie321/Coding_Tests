def remove_nodes(head) -> list:
    stack = []
    current = head

    while current:
        stack.append(current)
        current = current.next

    current = stack.pop()
    maximum = current.val
    result_list = maximum

    while stack:
        current = stack.pop()

        if current.val < maximum:
            continue
        else:
            new_node = current.val
            new_node.next = result_list
            result_list = new_node
            maximum = current.val

    return result_list