#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    all_dir = dir(hidden_4)
    for i in range(0, len(all_dir)):
        if "__" != all_dir[i][:2]:
            print(all_dir[i])
