# immutable
# once created you can't change the content.

## Perfom CRUD

# Create

colors = ("red", "green", "blue")

# Read elements for a tuple

# print(colors[0])
# print(colors[0:4])

# update
# Cannot directly update tuple

# updating a tuple requires you to create a new one

colors_two = ("yellow",)
print(colors[0])

print(type(colors_two))


# deleting
# cannot delete one item at a time.

# delete happens to the entire tuple

del colors

print(colors_two)
# print(colors)

