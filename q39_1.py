class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      res = []
      self.backtrack(candidates, target, 0, res, [])
      return res
    
    def backtrack(self, candidates, target, index, res, comb):
      if target == 0: 
        res.append(list(comb))
        return
      if target < 0: return
      if index >= len(candidates): return

      for i in range(index, len(candidates)):
        if candidates[i] > target: continue
        comb.append(candidates[i])
        self.backtrack(candidates, target - candidates[i], i, res, comb)
        comb.pop()
