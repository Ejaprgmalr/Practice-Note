def max_subarray(nums):
    """
      遍历array, 对每一个元素要判断, 是否加入到subarray里,
      是否重新开始一个subarray
      即比较和当前的subarray元素和的大小和短浅元素大小
    """
    current_val = nums[0]
    max_val = nums[0]
    for i in range(1, len(nums)):
        current_val = max(current_val + nums[i], nums[i])
        max_val = max(current_val, max_val)

    return max_val
