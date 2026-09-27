class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size())
            return false;
        unordered_map<char, int> hash_map;

        for(auto i : s)
        {
            if(hash_map.count(i))
            {
                hash_map[i]+=1;
            } else {
                hash_map[i] = 1;
            }
        }   

        for(auto i : t)
        {
            if(!hash_map.count(i))
                return false;
            else {
                hash_map[i] -= 1;
                if(hash_map[i] < 0)
                    return false;
            }
        }

        return true;
    }
};