class Codec:

    def serialize(self, root):
        vals = []

        def dfs(node):
            if not node:
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        if not data:
            return None

        vals = list(map(int, data.split(",")))

        def build(low, high):
            if vals and low < vals[0] < high:
                val = vals.pop(0)
                node = TreeNode(val)
                node.left = build(low, val)
                node.right = build(val, high)
                return node
            return None

        return build(float("-inf"), float("inf"))