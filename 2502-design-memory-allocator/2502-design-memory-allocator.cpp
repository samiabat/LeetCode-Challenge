class Allocator {
public:
    int arr[1000];
    int c[1001];
    int s = 0;
    
    Allocator(int n) {
        for (int i = 0; i<n; i++){
            c[i] = n - i;
            arr[i] = 0;
        }
        s = n;
        c[n] = 0;
    }
    
    int allocate(int size, int mID) {
        for (int  i = 0; i<s; i++){
            if (c[i] >= size){
                int j = i;
                while (j<s && j<i+size){
                    arr[j] = mID;
                    c[j] = 0;
                    j += 1;
                }
                return i;
            }
        }
        return -1;
    }
    
    int free(int mID) {
        int ans = 0;
        for (int i = 0; i<s; i++){
            if (arr[i] == mID){
                arr[i] = 0;
                ans += 1;
                int j = i;
                while (j>=0 && arr[j] == 0){
                    c[j] = (1 + c[j + 1]);
                    j -= 1;
                }
            }
        }
        
        return ans;
    }
};