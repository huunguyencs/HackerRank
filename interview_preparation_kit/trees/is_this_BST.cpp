/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.  

The Node struct is defined as follows:
	struct Node {
		int data;
		Node* left;
		Node* right;
	}
*/
	struct Node {
		int data;
		Node* left;
		Node* right;
	};
	bool checkBST(Node* root) {
        return check(root, -__INT_MAX__, __INT_MAX__);
    }
    bool check(Node* node, int min, int max){
        if (node == nullptr)
            return true;
        return min < node->data && node->data < max &&
            check(node->left, min, node->data) &&
            check(node->right, node->data,max);
    }