nums = [0,0,1,1,1,2,2,3,3,4,23,56,23,121,676,876,121]
output = []
for i in nums:
 if i not in output:
  output.append(i)

print(output)
