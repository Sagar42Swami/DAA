
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {
    address public owner;
    mapping(address => uint) private balances;

    // Constructor to set contract owner
    constructor() {
        owner = msg.sender;
    }

    // Deposit money to your account
    function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;
    }

    // Withdraw money from your account
    function withdraw(uint _amount) public {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        payable(msg.sender).transfer(_amount);
        balances[msg.sender] -= _amount;
    }

    // Show your account balance
    function showBalance() public view returns (uint) {
        return balances[msg.sender];
    }
}


// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    struct Student {
        uint rollNo;
        string name;
        uint age;
        string department;
    }

    Student[] public students;

    // Add a new student
    function addStudent(uint _rollNo, string memory _name, uint _age, string memory _dept) public {
        students.push(Student(_rollNo, _name, _age, _dept));
    }

    // Get student count
    function getStudentCount() public view returns (uint) {
        return students.length;
    }

    // Get student by index
    function getStudent(uint _index) public view returns (uint, string memory, uint, string memory) {
        require(_index < students.length, "Invalid index");
        Student memory s = students[_index];
        return (s.rollNo, s.name, s.age, s.department);
    }

    // Fallback function - runs if Ether is sent accidentally
    fallback() external payable {
        // This will prevent Ether loss and emit event
        emit Received(msg.sender, msg.value);
    }

    // Event to log Ether received
    event Received(address sender, uint value);
}
