class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count ={}
      #frequency of list of numbers array
      freq = [[] for i in range(len(nums)+ 1 )]
      # we do +1 because it starts with index 0 to nums-1

      #count the freq of numbers and append to the hashmap
      # we check the if the num of the list is present in the hashmap
      for num in nums:
        count[num] = 1 + count.get(num,0)
      for num, cnt in count.items():
        #key ,value in hashmap count
        #num=1 , cnt=2, freq[2]= go to bucket at index 2 
        #freq[2(index)] =[[],[],[1],[],[]]
         # we get the freq array[2]
        freq[cnt].append(num)

      res = []
      for i in range(len(freq) - 1, 0, -1):
            #highest index,stop, go backwards
            #i goes:7,6,5,4,3,2,1 but not 0 because sstop is exclusive
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res