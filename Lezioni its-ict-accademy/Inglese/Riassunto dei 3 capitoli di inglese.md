# Primo capitolo
## What is Computational Thinking?

**Definition and Origins**  
Computational Thinking (CT) is a way to solve problems using ideas from computer science, with the goal of creating solutions that computers can carry out. Defining CT has been tricky because it’s a broad concept. Some people want a clear definition, while others, like Voogt et al. (2015), think it should be more flexible, similar to how we define something as general as a "game." This flexibility shows that CT combines both abstract and practical ideas.

The idea of CT isn’t brand new. It started in the 1980s when Seymour Papert introduced "procedural thinking" using the Logo programming language. However, CT became more popular in 2006 after Jeannette Wing gave a talk about it. Since then, people have been discussing its role in education and other areas. Different definitions have emerged, focusing on things like breaking down problems, finding patterns, and using computational tools.

**Core and Peripheral Concepts**  
Cynthia Selby (2013) helped make CT clearer by dividing its ideas into **core** and **peripheral** parts. The core concepts, which are the most important, include:

- Logical thinking
    
- Algorithmic thinking (step-by-step problem-solving)
    
- Breaking problems into smaller parts (decomposition)
    
- Finding patterns and generalizing
    
- Creating models
    
- Simplifying problems (abstraction)
    
- Evaluating solutions
    

Peripheral concepts are useful but not central to CT. These include things like data representation, critical thinking, automation, and simulation/visualization.

**Applications Across Fields**  
CT isn’t just for computer science; it’s useful in many areas. For example:

- **Event planning**: Randy Bryant used CT to organize a graduation ceremony more efficiently by creating a "pipeline" for handing out diplomas (Wing, 2011).
    
- **Climate science**: Scientists use computational models to predict climate change (Furber, 2012).
    
- **Music**: A musician used sorting algorithms to organize sheet music, saving time during a performance (Wing, 2011).
    
- **Law**: Tools inspired by CT help police and judges analyze crime scenes (Bundy, 2007).
    

These examples show how CT can be used in many different fields to solve problems.

**Differences and Misunderstandings**  
CT is often confused with computer science or programming, but it’s different. Computer science is about how computers work, and programming is about writing software. CT, on the other hand, is a way of thinking about problems. It assumes a computer will help solve the problem, but its ideas—like breaking problems into smaller parts or finding patterns—can be used in many areas, not just coding.

As Barr and Stephenson (2011) point out, the goal of CT isn’t to make everyone think like a computer scientist but to give them tools to solve problems in any field.

**Current Challenges**  
CT still faces some challenges:

1. **It’s still developing**: CT is a relatively new idea, and its definition is still evolving.
    
2. **Effectiveness**: We don’t yet have enough evidence to show how well CT education works in the long term.
    
3. **Overclaiming**: Some people worry that CT is being presented as something only computer scientists can do. Many of its ideas, like logic and algorithms, have been used in other fields for a long time. It’s important not to act like computer science "owns" these ideas.
    

**Conclusion**  
Computational Thinking is a flexible and structured way to solve problems using ideas from computer science. It’s not just for programmers or tech experts—it can be used in many fields. As CT continues to grow, it could become a universal way to tackle complex problems in our digital world.


---

# Prima parte del secondo capitolo
## Logical and Algorithmic Thinking

### **Logical Thinking**

At the core of computational thinking is **logic**, which helps us tell the difference between good and bad reasoning. Logic is important because computers follow our instructions exactly, so we need to make sure our reasoning is correct.

A **premise** is a statement that can be true or false. For example:

1. Socrates is a man.
    
2. All men are mortal.
    
3. Therefore, Socrates is mortal.
    

Here, the first two statements are premises, and the third is the conclusion. Logic makes sure the conclusion makes sense, which is key when giving instructions to computers.
The request is not authorized because credentials are missing or invalid.
### **Deductive vs. Inductive Arguments**

There are two main types of logical arguments: **deductive** and **inductive**.

- **Deductive arguments** are very strong. If the premises are true and the reasoning is correct, the conclusion must be true. For example:
    
    1. All dogs are mammals.
        
    2. Missie is a dog.
        
    3. Therefore, Missie is a mammal.
        
    
    But if a premise is wrong, the conclusion can be wrong too. For example:
    
    1. All birds can fly.
        
    2. A penguin is a bird.
        
    3. Therefore, a penguin can fly.
        
    
    Here, the first premise is false, so the conclusion is wrong.
    
- **Inductive arguments** are based on probability, not certainty. They use evidence to support a conclusion, but it’s not guaranteed. For example:
    
    1. A bag has 99 red balls and 1 black ball.
        
    2. Sarah picked a ball.
        
    3. Therefore, Sarah probably picked a red ball.
        
    
    Inductive reasoning is useful when we don’t have all the information.
    

### **Boolean Logic**

Computers work with true/false or 1/0 values. **Boolean logic** is a system that fits this binary world, making it perfect for programming. In Boolean logic, statements (called **propositions**) can only be true or false.

- **Properties of Propositions**:
    
    - A proposition must be clear and specific. For example, "It is traveling fast" is too vague unless we define "fast" (e.g., over 70 mph).
        
    - Propositions can be combined using logical operators like AND, OR, and NOT.
        

### **Logical Operators**

Logical operators help us combine propositions and figure out if they’re true or false. The main operators are:

1. **AND**: Both statements must be true for the result to be true.
    
    - _Example_: "The game continues if at least one square is empty AND no player has won."
        
2. **OR**: At least one statement must be true.
    
    - _Example_: "The game ends if Player 1 OR Player 2 wins."
        
3. **NOT**: Reverses the truth value of a statement.
    
    - _Example_: "If a square is NOT occupied, a player can place their symbol."
        
4. **IMPLIES**: If the first statement is true, the second must also be true.
    
    - _Example_: "If a player wins, the game is over."
        
5. **IF AND ONLY IF**: Both statements must always have the same truth value.
    
    - _Example_: "The game is over IF AND ONLY IF all squares are occupied."
        

### **Symbolic Logic**

Natural language can be unclear, so **symbolic logic** uses symbols to make reasoning easier. For example:

- Let P = "At least one square is empty."
    
- Let Q = "No player has won."
    
- Let S = "The game continues."
    

The statement "If P AND Q, then S" can be written as:  
**P ∧ Q → S**

This makes complex reasoning simpler and clearer.

**Truth tables** are another tool in symbolic logic. They show all possible truth values of propositions and the results of logical operations. For example, the truth table for AND shows that the result is only true when both propositions are true:

|P|Q|P AND Q|
|---|---|---|
|True|True|True|
|True|False|False|
|False|True|False|
|False|False|False|

### **Why This Matters**

Logical thinking is the foundation of solving problems with computers. It ensures our reasoning is clear and correct, which is crucial when programming. By understanding deductive and inductive reasoning, Boolean logic, and symbolic logic, we can create reliable solutions to complex problems.


---

# Seconda parte del secondo capitolo

## Logical and Algorithmic Thinking (Part 2)

This section dives deeper into the role of logical thinking and algorithmic decision-making in computational processes. It highlights how structured reasoning and precise logic are essential for creating effective algorithms and avoiding common pitfalls.

### **Algorithmic Decision-Making**

At the core of every algorithm lies **decision-making**. Algorithms rely on conditions to control loops, make choices, and determine the flow of execution. For example, in a simple game like **Noughts and Crosses (Tic-Tac-Toe)**, the algorithm must decide when to place a mark, check for a win, or end the game. These decisions are guided by logical conditions, such as "If a player has three marks in a row, declare them the winner."

### **Common Logical Mistakes ("Gotchas")**

Even with a solid understanding of logic, it’s easy to make mistakes when translating ideas into algorithms. Here are some common pitfalls and how to avoid them:

1. **Clarity and Precision**:  
    Computers follow instructions literally, without any common sense. Vague or incomplete instructions can lead to unexpected errors.
    
    - _Example_: Telling a computer to "sort the list" without specifying the order (ascending or descending) will result in ambiguity.
        
    - _Solution_: Always provide clear, unambiguous instructions. For instance, "Sort the list in ascending order."
        
2. **Misuse of Logical Operators**:  
    Words like "AND," "OR," and "NOT" can have different meanings in natural language compared to their strict logical definitions.
    
    - _Example_: In everyday speech, "Surname begins with A and B" might imply surnames starting with either A or B. However, in logic, "AND" means both conditions must be true simultaneously, which is impossible here.
        
    - _Solution_: Use logical operators carefully, ensuring they align with their formal definitions.
        
3. **Incomplete "IF-THEN" Statements**:  
    Algorithms must account for all possible conditions. Leaving out certain cases can lead to incorrect or incomplete results.
    
    - _Example_: A grading system that only assigns a "pass" grade without handling "fail" cases will fail to produce accurate results.
        
    - _Solution_: Ensure all conditions are covered. For example, "If the score is above 50, assign 'pass'; otherwise, assign 'fail.'"
        

### **Complex Conditionals and Precedence**

As algorithms grow more complex, so do their logical conditions. Proper use of **parentheses** and **precedence rules** is crucial to avoid ambiguity and ensure the correct order of operations.

- _Example_: Consider a grading algorithm that assigns an "ordinary pass" to students scoring above 50 but below 80, and a "distinction" to those scoring 80 or above. If the conditions are not structured correctly, a student scoring 85 might incorrectly receive an "ordinary pass" instead of a "distinction."
    
- _Solution_: Use parentheses to explicitly define the order of evaluation. For example:
    
    Copy
    
    IF (score >= 80) THEN assign "distinction"  
    ELSE IF (score >= 50) THEN assign "ordinary pass"  
    ELSE assign "fail"  
    

### **Key Takeaways**

- **Precision is key**: Computational thinking relies on clear, unambiguous logic. Avoid vague instructions and ensure all conditions are explicitly defined.
    
- **Symbolic logic over natural language**: Using formal logic and symbols helps eliminate ambiguity and ensures consistency in algorithms.
    
- **Master Boolean logic and conditionals**: Understanding how logical operators work, along with proper use of parentheses and precedence, is essential for writing correct and efficient programs.
    

By paying attention to these principles, you can avoid common logical errors and create algorithms that are both reliable and effective.


---
# Terzo capitolo
## Problem-Solving and Decomposition

### **Breaking Down Complex Problems**

When faced with a complex problem, one of the most effective strategies is **decomposition**. This approach involves breaking a large, overwhelming problem into smaller, more manageable sub-problems. By dividing the problem into discrete components, each part can be addressed independently, making the overall task less daunting and more approachable. Decomposition also facilitates collaboration, as different individuals or teams can work on separate parts simultaneously.

However, decomposition alone doesn’t always provide clarity on the order in which tasks should be tackled. For example, in software development, breaking a project into modules is helpful, but it doesn’t inherently tell you whether to start with the user interface, the database, or the backend logic. To address this, decomposition is often paired with other problem-solving strategies.

### **Key Problem-Solving Strategies**

In addition to decomposition, several strategies can help tackle complex problems effectively:

1. **Critical Thinking**  
    Critical thinking involves evaluating ideas objectively, questioning assumptions, and ensuring that every decision is well-justified. This is especially important in system design, where incorrect assumptions can lead to inefficient or flawed solutions. For instance, when designing a library management system, it’s crucial to ask whether the chosen data organization method truly meets the needs of the users.
    
2. **Pattern Recognition**  
    Recognizing recurring patterns within a problem allows you to apply solutions that have worked in similar situations. This is a common practice in programming, where developers identify familiar algorithmic patterns—such as searching, sorting, or recursion—and reuse established solutions rather than starting from scratch.
    
3. **Abstraction**  
    Abstraction is the process of focusing on the essential details of a problem while ignoring unnecessary complexities. This is particularly useful in algorithm design, as it enables the creation of generalized solutions that can be adapted to a wide range of scenarios. For example, when designing a sorting algorithm, you might abstract away the specific data types and focus on the core logic of comparing and rearranging elements.
    
4. **Algorithmic Thinking**  
    Algorithmic thinking involves developing step-by-step procedures to solve problems efficiently. It requires logical reasoning to determine the best approach, whether through brute force, heuristics, or optimization techniques. For example, when planning a route, algorithmic thinking helps you evaluate different paths and choose the most efficient one.
    

### **Combining Strategies for Effective Solutions**

While decomposition is a powerful tool, it’s most effective when combined with other problem-solving strategies. For instance, after breaking down a problem into smaller parts, you might use **critical thinking** to evaluate the feasibility of each component, **pattern recognition** to identify reusable solutions, **abstraction** to simplify complex details, and **algorithmic thinking** to design efficient processes.

By integrating these strategies, individuals and teams can approach complex problems in a structured, efficient, and scalable way. This not only makes problem-solving more manageable but also increases the likelihood of arriving at effective and innovative solutions.