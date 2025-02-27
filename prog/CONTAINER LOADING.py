def container_loading(items, container_capacity):
    container = []
    current_weight = 0
    for item in items:
        if current_weight + item <= container_capacity:
            container.append(item)
            current_weight += item
    return container
items = [20, 10, 30, 5, 15]
container_capacity = 50
loaded_container = container_loading(items, container_capacity)
print(loaded_container)
