# Modern approaches to programming

Modern programming has an organic, layered feel to it that may come as a surprise. In this course, we will learn how to read through the layers to understand how programs are built and how to build our own. Let us start with some very basic questions.

## What is a computer ?

A classical computer is an engine of some kind for processing pure information. Various components are needed to make this possible including some means of initialising and storing the information before and after it is processed, and a mechanism for processing information (including the case where the processing is dependent upon the information itself). Many different machines can meet these criteria but we usually add at least one more requirement: the computers that we are interested in are *programmable* in that they can be given different instructions that describe what processing will be done. 

The original **Analytical Engine** designed by Babbage and Lovelace in the 1830s (see {cite}`babbage_babbages_2010`) fits these criteria and so do most modern digital computers. One of the pioneers of computing information theory, John von Neumann, describes the necessary requirements for a true computer and makes many very interesting comparisons between the digital computers of his time (the 1950s) and the human brain in his final book *Computing and the Brain* 
{cite}`von_neumann_computer_2012`.

There are many kinds of computers that we will not be discussing such as the embedded systems in controllers, engines, cars, aircraft and so on. Some of these might use recognisable programming but many are heavily focused on the job that they must do quickly, with low overhead and no danger of crashing as they process critical information in real time. These systems may well have more in common with early electronic computers because complexity can be the enemy of reliability or at least of demonstrating reliability in the face of every conceivable input. 

We will also make an assumption that there is only one information processing engine that we are programming at any one time. Most computers are, in fact, multiple processing engines that work simultaneously either on different tasks that do not interact or on subsets of the information that are isolated from each other. Real parallel programming almost always requires us to understand and control how those data or task interdependencies work and that is an a subject in its own right.

## What is a programming language ?

Broadly speaking, a programming language is a way to tell a computer how to obtain and process information for us. There are two distinct paradigms in programming that approach problems in quite different ways. 

The first of these is the **declarative** approach which states what needs to be done and does not say very much about how it needs to be done. Some examples of this are "Hey Siri ..." or "Hey Google ..." followed by some question such as "will it be hot today ?" and we expect some sort of reasonable response to that without further explanation. Another example is a spreadsheet where calculations mostly just happen without having to explain in detail how to sum a column or multiply two columns. This is also the way we usually interact with human experts !

The second paradigm is usually less familiar in our everyday experience. **Imperative** programming is what happens when you lay out every step in detail for the computer to follow and these steps will be followed *to the letter* no matter what mistakes you make in giving the instructions. We don't give instructions to people at this level unless they have no experience whatsoever in some topic. "Would you make me a cup of tea, please ?" becomes "Walk from your current position to the kitchen and identify the kettle, turn the on/off switch to the on position ... " and so on. Any of these steps is open to misinterpretation and misunderstanding so how do you know when to stop adding more details ? 

Imperative programming is the way we will approach most science problems but we will also be making use of many libraries and modules that *have already encoded* the basic instructions for the kinds of tasks we want to do. Our job is often just trying our best to find these libraries, test them and work out all the things they can do. The many layers of abstraction are a way to know the appropriate level of detail in describing a task. 

A programming language is just a way to make the writing and executing of these instructions as simple and re-usable as makes sense for the task in hand. Some are very low level for programming individual chips, and some are very high level if, for example, we want to build an interactive website quickly and mostly according to a pre-existing recipe. Some programming languages trade ease of use for speed (languagues like `C` and `Fortran` are like this) and some are very flexible but have to do a lot of checks when they run to make sure all the ideas fit together consistently (`Python` is like that, and so is `Perl`). Some programming languages are just arrangements of logical blocks where we specify the operations and their interactions but not in text form (e.g. `scratch`) but they are still, at some level, explaining what to do, in what order, to which pieces of data.

We are going to concentrate on `Python` which is a flexible language that is widely used by the scientific community. I has a few things in common with English, actually, in that it is very good at absorbing concepts from other languages, and there are always many different ways to say something. `Python` makes it possible to create levels of abstraction that hide unimportant details but those details are not particularly well hidden and it is always possible to dig down and find out more. 

## What does a well-written program or library look like ?

One of the first questions to ask before starting to write some code is "did somebody already write this ?" and, if the answer is yes, can you quickly work out which of these options is best:
  - Use the existing program or library
  - Modify the existing program or library
  - Start again

If you do decide to use somebody else's code, you will need to understand how it works and check that it really does work as advertised. If you need to modify the code, you should consider whether you are going to contribute those improvements back to the author or the community. 

Going through this process for somebody else's code is also a very good idea before you write your own code because, honestly, it helps you to be as critical of your own work as you would be of others. Here is a checklist that feels a lot more intimidating if you imagine scrutinising your own programs, not somebody else's:

  - Can I find the source code ?
  - Is the source code clear, readable with comments ?
  - Is there a suite of tests with good coverage of the code ?
  - Are the benchmarks or verifications of inputs v. outputs ?
  - Is there clear documentation for a typical user or a typical developer?
  - Is it clear how bug-fixes and improvements will be accepted ?
  - Is the code up-to-date with the latest operating systems ?

The discussion so far gets us to the point where we know how to describe what we want from a piece of software even if we don't know how to build it ourselves (another layer of abstraction, by the way) !  You are going to be encouraged to approach any task from this high level view. We will always start with the question - has somebody done this already ?

## How do we work in a world of re-usable computing ?

Our goal is to learn not just how to program a computer but how to write software that works and with all the tests to prove that it works; software that other people will find helpful and that they will be encouraged to use. 
That is to say, software that is "well-written" by the criteria we just discussed. 

We will touch upon *literate programming* which is a way to interweave rich documentation (with full text, equations, images etc) into code so that it is automatically well explained and properly documented and also to ensure that the documentation and the code do not drift apart when changes are made.

We will discuss the benefits of making codes open-source and hosting them on a public repository so that they are easily discoverable. We will discuss version control and testing and the benefits of merging those two things into one process so that you can be sure each change you make to the code does not introduce errors in other parts of the code. 



