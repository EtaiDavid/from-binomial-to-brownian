# Mathematical Theory - From Binomial to Brownian Motion

This document contains the mathematical foundation for understanding the convergence from discrete binomial models to continuous-time stochastic processes. We start from the absolute fundamentals and build up carefully, ensuring that each concept is thoroughly understood before moving to the next.

## Foundational Concepts - Building from the Ground Up

### What Does "Stochastic" Mean?

Before we can understand random walks, Brownian motion, or option pricing models, we must first understand what the word "stochastic" means. This word appears constantly in quantitative finance, probability theory, and mathematical modeling, yet its precise meaning is often taken for granted.

The word "stochastic" is derived from the Greek word "stochastikos," which means "skillful in aiming" or "proceeding by guesswork." In modern mathematical usage, stochastic simply means **random** - something that involves uncertainty, something whose outcome we cannot predict with certainty in advance. But this simple translation hides a crucial subtlety that we must understand.

When we say something is stochastic or random, we do not mean it is arbitrary or chaotic or without structure. There is a fundamental difference between randomness and arbitrariness. Consider the following two scenarios to see this distinction clearly.

**Scenario One: Rolling a Fair Die**

Imagine you are about to roll a standard six-sided die. You do not know which number will appear - it could be one, two, three, four, five, or six. The outcome is uncertain. It is random. But notice that this randomness has structure. You know with certainty that the result will be one of these six numbers - it will not be seven, it will not be negative, it will not be a fraction. Furthermore, if the die is fair, you know that each outcome has an equal probability of one-sixth. If you were to roll the die many times, you could predict with confidence that roughly one-sixth of the rolls would show each number, and the average result would be close to 3.5.

This is stochastic randomness. The individual outcome is uncertain, but the process follows probabilistic rules. There is a well-defined **probability distribution** governing the outcomes.

**Scenario Two: Arbitrary Choice**

Now imagine instead that I ask you to give me any number you like. You could say five. You could say negative one million. You could say the square root of two or pi. There are no constraints, no probabilities, no structure. This is not stochastic randomness - this is pure arbitrariness. There is no probability distribution that describes your choice because you are not selecting according to any random mechanism. You are making an unconstrained, deterministic (even if unpredictable to me) choice.

**The Key Distinction**

The essential difference is this: something is stochastic if its outcome is governed by a probability distribution. When we use the word "stochastic," we are implicitly asserting that there exists a mathematical framework - probability theory - that describes the uncertain quantity. We may not know what will happen, but we know the rules that govern what can happen and how likely each possibility is.

This is why we can do mathematics with stochastic phenomena. We cannot predict the individual outcome of a coin flip, but we can say with mathematical precision that the probability of heads is one-half. We cannot predict tomorrow's stock price, but if we model it as following a certain stochastic process, we can make statements about the probability distribution of future prices. The randomness is constrained by mathematical structure.

**A Practical Test of Understanding**

Here is a way to check if you truly understand this distinction. If someone tells you they will select a number "stochastically," what can you conclude? You know that you cannot predict the exact number they will select - that is the essence of randomness. But you also know that somewhere, explicitly or implicitly, there is a probability distribution. You could ask them: "What is the probability distribution you are using?" and this question would make sense. If they say "I am choosing uniformly between zero and one," you now know that every number in that interval is equally likely, and numbers outside that interval have zero probability. If they say "I am choosing according to a standard normal distribution," you know that numbers near zero are most likely and extreme values become increasingly rare.

In contrast, if someone says they will select a number "arbitrarily," asking for a probability distribution makes no sense. There is no probabilistic structure governing their choice.

### What is a Stochastic Process?

Now that we understand what "stochastic" means, we can build the next layer: what is a **stochastic process**? This concept is the foundation for everything we will study in this project - random walks, Brownian motion, stock price models, and option pricing.

A stochastic process is a mathematical object that describes how some random quantity evolves over time. Think of it as a movie rather than a photograph. A random variable gives you a single random number - like the result of one die roll. A stochastic process gives you a sequence of random numbers indexed by time - like the results of rolling a die at time one, time two, time three, and so on.

**Formal Definition**

More formally, a stochastic process is a collection of random variables indexed by time. We typically denote a stochastic process by something like X(t) or Xₜ, where t represents time. For each value of t, X(t) is a random variable. If we observe the process over time, we get a sequence of random values - this sequence is called a **realization** or a **path** or a **sample path** of the process.

Let us unpack this definition carefully because each part is important.

First, notice that we have "random variables indexed by time." Time can be either discrete or continuous. In discrete time, we might have X₀, X₁, X₂, X₃, and so on - values at specific time points like zero, one, two, three. In continuous time, we have X(t) for every real number t in some interval, like all t between zero and T. Discrete-time processes are often easier to understand and work with, which is why we start with them. Continuous-time processes are often more realistic models of nature but require more sophisticated mathematics.

Second, for each time t, the quantity X(t) is a **random variable**. This means that if we were to observe the process at time t, we would see a random outcome drawn from some probability distribution. The distribution might depend on t - for instance, the randomness at time ten might be different from the randomness at time one.

Third, and most subtly, the random variables at different times are typically not independent of each other. What happens at time five might depend on what happened at time four. In fact, this dependence over time is what makes stochastic processes interesting and useful as models. If the values at different times were completely independent, the process would just be a sequence of unrelated random draws - not very interesting. The dependency structure is what allows a stochastic process to model things like stock prices, where tomorrow's price depends on today's price, or weather patterns, where tomorrow's temperature is related to today's temperature.

**An Intuitive Example: Temperature Over Time**

Let us make this concrete with an example that has nothing to do with finance. Consider the temperature in your city over the course of a year. Each day has a temperature, and you can think of this as a stochastic process where t represents the day number and X(t) represents that day's high temperature.

Why is this a stochastic process? Because the temperature on any given day is not deterministic - we cannot predict it exactly in advance. There is randomness. But this randomness has structure. The temperature on July 15th is unlikely to be freezing because summer temperatures follow a certain distribution. The temperature tomorrow is likely to be close to today's temperature because weather patterns change gradually, not abruptly. If we observed this temperature process over many years, we could estimate probability distributions for each day's temperature, and we could model the dependence structure that makes consecutive days' temperatures correlated.

This is the essence of a stochastic process - a sequence of random observations over time, where the randomness is structured by probability distributions and often exhibits dependence across time.

**Why Do We Care About Stochastic Processes?**

Stochastic processes are the mathematical language for describing anything that evolves randomly over time. Stock prices evolve randomly - we model them as stochastic processes. Interest rates change unpredictably - stochastic processes. The number of customers arriving at a store each hour - stochastic process. The position of a particle jiggling around due to molecular collisions (Brownian motion) - stochastic process.

Once we model something as a stochastic process, we can use the powerful machinery of probability theory and stochastic calculus to answer questions. What is the probability that a stock price will reach a certain level? What is the expected value of an option at expiration? What is the risk of a portfolio over the next month? All of these questions are answered using the theory of stochastic processes.

### First Example: A Simple Coin-Flipping Process

Before we define random walk formally, let us consider the simplest possible stochastic process to solidify our understanding. Imagine we flip a fair coin repeatedly - at time one, time two, time three, and so on. Let X(t) equal one if the t-th flip is heads and zero if it is tails. This is a stochastic process.

At each time t, X(t) is a random variable that equals zero or one, each with probability one-half. The values at different times are independent - knowing that flip five was heads tells us nothing about flip six. This is a particularly simple stochastic process because of this independence, but it is a stochastic process nonetheless.

Now let us define a related process: let S(t) equal the total number of heads we have seen up through time t. So S(1) equals X(1), and S(2) equals X(1) plus X(2), and S(3) equals X(1) plus X(2) plus X(3), and so on. Formally, S(t) equals the sum of X(1) through X(t). This new process S(t) is also stochastic, but it has different properties. Unlike the original flip process, the values of S(t) are not independent over time - if S(5) equals four, then S(6) must be either four or five, because we can only add zero or one to the previous value.

This cumulative process S(t) is similar in spirit to a random walk, which we are about to define formally. But first, let us pause and check understanding.

## Part 1: Random Walk - The Discrete Foundation

Now that we have established what "stochastic" means and what a "stochastic process" is, we are ready to define our first specific example: the random walk. The random walk is one of the most important stochastic processes in all of mathematics. It appears in physics, biology, economics, computer science, and countless other fields. For our purposes, it is the foundation upon which we build our understanding of option pricing.

## Why Study Random Walks? The Connection to Finance and Real-World Phenomena

Before we dive into the formal mathematics, we must answer a fundamental question: why do we care about random walks? What does a coin flip have to do with stock prices or option pricing? This is not just an academic exercise - understanding this connection is crucial for seeing why we are spending so much time on these mathematical properties.

**What Does Position Represent in the Real World?**

When we talk about the "position" in a random walk, we are not discussing an abstract mathematical concept. Position represents the accumulation of random changes over time. Think of it this way - at each moment, something small and random happens, and all these random changes accumulate. The position at time t is the sum of everything that has happened up to now.

Consider a dust particle floating in still air inside a room. The particle receives random impacts from air molecules from all directions. Each impact is a small random "step" in some direction. Where is the particle after one minute? That is the position - the cumulative effect of all the random impacts. Where will it be after ten minutes? That is the position at time ten minutes. This position tells us something important - how far the particle has drifted from where it started. This is actual physical Brownian motion, and the mathematics of random walks describes it precisely.

Or consider daily temperature. Each day's temperature is affected by many small random factors - winds, clouds, humidity. If we start with a certain temperature and experience small random changes each day, where will the temperature be after a month? That is the position - the accumulated temperature after all the random changes. How far has it deviated from the starting temperature? That is what position tells us.

**The Critical Connection to Stock Prices - Why You Are Learning This**

Now let us arrive at what is truly relevant to quantitative finance. A stock price follows exactly the same principle. Think about a stock that starts at a certain price, say one hundred dollars. Every day, every hour, every second - new information arrives, the market reacts, someone buys, someone sells. The price moves up a little or down a little. Each such small change is like a "step" in a random walk. Where will the price be after a month? That is the position - the accumulation of all the small random changes that occurred. Where will the price be after a year? That is the position at time one year.

The position at time t tells us something critical - how much the price has changed from the starting price. If we started at one hundred dollars and the position after a year is plus twenty, the price is one hundred twenty dollars. If the position is minus fifteen, the price is eighty-five dollars. The position is essentially the cumulative return. And all the mathematics of random walks teaches us how this position evolves, how it spreads out, what the probability is that it reaches various values.

This is exactly why this project discusses "from binomial to Brownian motion" and "option pricing." This model of random walks is the foundation for the famous Black-Scholes model for pricing options. All of it flows directly from understanding how prices wander randomly over time.

**An Important Clarification: Real Stock Prices Have Drift**

However, we must be precise about something important. Real stock prices do not follow a symmetric random walk exactly. In a symmetric random walk, the expected position is always zero - meaning on average, you expect to end up where you started. But in reality, stocks on average rise over time. There is a positive average return. So how can the random walk model describe stock prices?

The answer is that the realistic model is not a symmetric random walk, but a random walk with drift. This means that at each step, there is a bias in one direction. Instead of probabilities being one-half to go up and one-half to go down, perhaps the probability to go up is fifty-three percent and to go down is forty-seven percent. This small difference accumulates over time and creates an average movement in one direction.

Why then do we start with the symmetric case? Because the symmetric random walk teaches us the mathematics of the random component of price movements. Even when there is drift, all the properties we learn - variance growing linearly, distribution approaching normal, spreading proportional to square root of time - remain true for the random component. The drift adds a trend, but the randomness around the trend behaves exactly like a symmetric random walk.

In the Black-Scholes model, stock prices are modeled as following geometric Brownian motion with drift. The "Brownian motion" part comes from the symmetric random walk we are studying. The "drift" part accounts for the average positive return. Both components are necessary for a realistic model, but understanding the symmetric case first gives us the foundation for understanding the random fluctuations that drive option prices.

**Why Normal Distribution Matters - The Heart of the Story**

Now for the second part of the motivation: why does it matter so much that the distribution of position becomes normal? This is truly the key point of everything.

Imagine you hold a call option on a stock. The option gives you the right to buy the stock at one hundred dollars in three months. The most important question is - how much is this option worth today? To answer this, you need to know something very specific - what is the distribution of possible prices in three months.

Without knowing the distribution, you cannot calculate anything. You need to know - what is the probability that the price will be one hundred ten? What is the probability it will be ninety? One hundred fifty? If you do not have a probability distribution, you have no way to calculate the expected value of the option, and no way to price it.

And here is exactly where the fact that the distribution is normal enters the picture. Why is this so powerful? Because the normal distribution is one of the simplest and most convenient distributions to work with mathematically. It is completely characterized by just two parameters - the mean and the variance. If you know these two parameters, you know everything about the distribution. You can calculate any probability you want.

For example, if you know that position is normally distributed with mean zero and variance one hundred, you can use a normal distribution table (or statistical functions in any computer software) and immediately calculate - what is the probability that position will be greater than fifteen? What is the probability it will be between minus ten and plus ten? Every such calculation becomes simple and straightforward.

There is something else very important. The normal distribution is closed under certain mathematical operations. For instance, if you have two independent normal random variables and you add them, the sum is also normal. This gives us very powerful analytical tools. We can perform complex mathematical calculations on normal processes and arrive at explicit solutions.

This is why the Black-Scholes model works. They assumed that stock prices follow geometric Brownian motion, which is essentially a continuous-time random walk with the logarithm of price being normally distributed. Given this assumption about the distribution, they were able to derive a closed-form, explicit formula for the price of an option. Without the assumption that the distribution is normal, the formula would not exist. The mathematics simply would not work out.

**Why the Central Limit Theorem Is So Important**

Now you can understand why the third property - that the distribution approaches normal - is so central. It tells us that any process built from many small, independent random changes will eventually behave as if it is normal. It does not matter how each individual change is distributed - the sum will be approximately normal.

This is profound justification for using the normality assumption in financial models. If a stock price changes due to thousands of small, independent factors - buy and sell orders, news, speculation, market sentiment - then the Central Limit Theorem guarantees us that the accumulation of all these changes will look normal. This is not an arbitrary assumption; it is a deep mathematical result.

**The Connection to Risk Management**

There is another important aspect relevant to practical finance. When you know the distribution of future prices, you can calculate risks. What is the probability that an investment portfolio will lose more than ten percent next week? If you know that returns are normally distributed, you can calculate this precisely. This is Value at Risk, this is stress testing, these are all the tools that banks use to measure and manage risks.

If the distribution were unknown, or if it were something complicated and non-normal, all these calculations would become very difficult or impossible. Normality gives us the tools to work with uncertainty in a quantitative and precise way.

**Summary of Motivation**

So in summary: we study the position in random walks because it represents the accumulation of random changes over time - which is exactly what financial asset prices do. Position tells us where the asset is after a certain period, how much it has risen or fallen, what the cumulative return is.

And we care deeply that the distribution is normal because this gives us the mathematical tools to price assets, calculate risks, and manage portfolios. Without normality, all of modern financial mathematics would not work. It is the cornerstone upon which the Black-Scholes model, portfolio management, risk management, and almost the entire field of quantitative finance are built.

With this motivation firmly in place, we are ready to study the formal properties of random walks. Every property we learn has direct applications to understanding how prices move and how to value financial instruments.

### Formal Definition of a Symmetric Random Walk

A symmetric random walk is a discrete-time stochastic process defined as follows. We start at position zero at time zero. At each subsequent time step, we move either one unit to the right or one unit to the left, each with probability one-half. The position after n steps is the sum of all the individual steps taken.

Let us write this more formally with mathematical notation. Let S₀ equal zero - this is our starting position. At each time n equals one, two, three, and so on, we generate a random step Xₙ that equals plus one with probability one-half or minus one with probability one-half. These steps are independent - the result of step seven does not depend on the results of steps one through six. The position at time n is defined as Sₙ equals the sum of all steps, which we write as Sₙ equals X₁ plus X₂ plus ... plus Xₙ. We can write this more compactly using summation notation as Sₙ equals the sum from i equals one to n of Xᵢ.

This simple definition completely specifies the random walk. Given this definition, we can answer any probabilistic question about the walk - what is the probability that S₁₀ equals four? What is the expected value of S₅₀? What is the probability that the walk ever reaches ten? All of these questions have precise mathematical answers that follow from the definition.

**Understanding the Definition Through Visualization**

It helps to visualize what a random walk looks like. Imagine you are standing at zero on a number line. You flip a coin. If it is heads, you step to the right and move to position one. If it is tails, you step to the left and move to position minus one. You flip again. If heads, you move one unit right from your current position. If tails, you move one unit left. You continue this process.

Your sequence of positions forms a path - a sequence of integers that wanders up and down the number line. If you were to plot this path on a graph with time on the horizontal axis and position on the vertical axis, you would see a jagged line that steps up or down by one unit at each time point. This is a realization or a sample path of the random walk.

If you were to repeat this entire process from the beginning with new coin flips, you would get a different path. The two paths would start at the same place (zero) but would quickly diverge as the random coin flips differ. Each repetition gives you another sample path of the random walk. The random walk as a stochastic process encompasses all possible such paths, weighted by their probabilities.

### Why "Symmetric"?

We specified that this is a "symmetric" random walk because the probabilities of stepping right and stepping left are equal - both are one-half. This symmetry has important consequences, the most important being that the expected position stays at zero for all time. There are also asymmetric random walks where the probability of stepping right is p and the probability of stepping left is one minus p, where p is not equal to one-half. Such walks have a drift - they tend to wander in one direction over time. For our purposes, we focus on the symmetric case because it is simpler and because it is the foundation for Brownian motion, which is also symmetric in a certain sense.

### Why Start with Random Walk?

At this point you might reasonably ask: why are we spending so much time on this simple process of coin flips and steps? The answer lies in the remarkable fact that this simple discrete process, when properly scaled and taken to a limit, becomes Brownian motion - the continuous-time stochastic process that underlies the Black-Scholes model and much of modern finance.

The random walk is discrete in two senses. First, it is discrete in time - we take steps at time one, two, three, and so on, not continuously. Second, it is discrete in space - we can only be at integer positions, not at arbitrary real numbers. These discretizations make the random walk easy to define, easy to simulate, and easy to reason about mathematically. We do not need advanced calculus or measure theory to work with random walks - just basic probability.

But real-world phenomena are often better modeled as continuous. Stock prices can change at any moment, not just at discrete time intervals. They can take on any positive value, not just discrete increments. This is where Brownian motion comes in - it is continuous in both time and space. And remarkably, Brownian motion is exactly what you get when you take a random walk, scale it appropriately, and take a limit as the step size goes to zero and the number of steps goes to infinity.

Understanding random walk deeply prepares us for understanding Brownian motion. Many properties of Brownian motion - the fact that its expected value stays at zero, that its variance grows linearly with time, that its increments are normally distributed - are inherited from the random walk in the limit. By mastering the discrete case first, we build intuition for the continuous case.

Furthermore, the binomial model for option pricing, which you worked with in your previous course, is essentially a random walk applied to stock price ratios. The stock price at each node of the binomial tree either goes up or goes down by fixed factors - this is a multiplicative random walk. When we price options using binomial trees with many periods, we are approximating the continuous Black-Scholes price. The convergence of binomial prices to Black-Scholes prices is intimately related to the convergence of random walks to Brownian motion.

So the random walk is not just a cute example or a toy model. It is the discrete foundation for all of continuous-time finance. Master it, and you have the key to understanding everything that follows.

### Fundamental Mathematical Properties of the Symmetric Random Walk

Now that we have defined what a random walk is, we must understand how it behaves. A mathematical definition is just the starting point - the real understanding comes from knowing the properties that follow from that definition. The symmetric random walk, despite its simplicity, exhibits rich mathematical behavior that will reappear in more sophisticated forms when we move to Brownian motion and option pricing models.

We will examine four fundamental properties in exhaustive detail. Each property tells us something essential about how random walks behave, and each will have an analogue in continuous time. We will not rush through these. Instead, we will take the time to understand not just what each property says, but why it is true, what it means intuitively, and why it matters for what comes later. Understanding these properties thoroughly is not optional - they are the foundation for everything that follows.

Before we begin, let us remind ourselves of some basic terminology that we will use repeatedly. When we say "expected value" or "expectation," we mean the average value we would get if we repeated the random process many times. When we say "variance," we mean a measure of how spread out the values are around the expected value. When we say "distribution," we mean the pattern of probabilities across all possible outcomes - it tells us which outcomes are likely and which are rare. With these reminders in place, let us proceed to the properties.

**Property One: The Expected Position is Always Zero**

**Statement of the Property**

The first property states that at any time n, the expected value of the position is zero. We write this mathematically as E[Sₙ] = 0 for all n. This is true whether n equals one, ten, one hundred, or one million. No matter how many steps we take, if we average over all possible random walks, the average position is exactly zero.

**Why This Property is True: The Mathematical Derivation**

Let us understand why this property holds by working through the mathematics step by step, starting from the definition. Recall that the position after n steps is defined as Sₙ = X₁ + X₂ + ... + Xₙ, where each Xᵢ is a random step that equals plus one or minus one with equal probability.

First, let us compute the expected value of a single step. By the definition of expectation, E[Xᵢ] equals the sum of each possible value times its probability. The step Xᵢ can take two values: plus one with probability one-half, and minus one with probability one-half. Therefore, E[Xᵢ] = (1/2)(+1) + (1/2)(-1) = 1/2 - 1/2 = 0. Each individual step has expected value zero because it is equally likely to go up as to go down. The positive and negative possibilities cancel out exactly in the average.

Now we need to find the expected value of the sum Sₙ = X₁ + X₂ + ... + Xₙ. Here we use a fundamental rule of expectation called linearity. Linearity states that the expected value of a sum equals the sum of the expected values. Mathematically, E[X₁ + X₂ + ... + Xₙ] = E[X₁] + E[X₂] + ... + E[Xₙ]. This rule is powerful and somewhat surprising because it works regardless of whether the random variables are independent or dependent. We do not need independence for linearity of expectation to hold.

Applying this rule to our random walk, we get E[Sₙ] = E[X₁ + X₂ + ... + Xₙ] = E[X₁] + E[X₂] + ... + E[Xₙ] = 0 + 0 + ... + 0 = 0. Since each step has expected value zero, the sum of n steps also has expected value zero. This completes the proof.

**What This Property Means: The Intuitive Interpretation**

Now that we know why the property is true mathematically, let us understand what it means intuitively. When we say the expected position is zero, we are making a statement about averages over many random walks, not about what happens in a single walk. 

Imagine you generate ten thousand independent random walks, all starting at zero, and you let each one run for one hundred steps. After those one hundred steps, you record the final position of each walk. Some walks will have ended far to the right - perhaps at position plus thirty or plus forty. Some will have ended far to the left - perhaps at position minus thirty or minus forty. Some will be near zero. If you take all ten thousand final positions and compute their average, that average will be very close to zero. As you increase the number of walks you generate, the average gets closer and closer to exactly zero.

This is what "expected position is zero" means. It is a statement about the center of mass of all possible outcomes, weighted by their probabilities. It does not mean that a typical walk stays near zero. In fact, as we will see in the next property, a typical walk wanders quite far from the origin as time goes on.

**What This Property Does Not Mean: A Critical Distinction**

We must be very careful about a common misunderstanding. The fact that E[Sₙ] = 0 does not mean that you should expect to find yourself near position zero after n steps. To see why, consider a simple example. Suppose you flip a coin once. If heads, you go to plus one. If tails, you go to minus one. The expected position is E[S₁] = (1/2)(+1) + (1/2)(-1) = 0. But you are never actually at position zero! You are always at either plus one or minus one. The expected value is zero, but that is not where you end up.

The same principle applies for larger n, though the situation becomes more nuanced. After one hundred steps, the expected position is still zero, but the possible positions are spread out widely. You might be at plus twenty, minus fifteen, plus five, minus thirty, or anywhere in between. The average of all these possibilities is zero, but an individual walk is typically nowhere near zero.

The expected position tells us about the center of the distribution, not about the spread. To understand how far walks typically wander, we need the next property, which concerns variance.

**Property Two: Variance Grows Linearly with Time**

**Statement of the Property and Why Variance Matters**

The second property states that the variance of the position at time n is exactly n. We write this as Var(Sₙ) = n. While the expected position stays fixed at zero for all time, the uncertainty about the position grows steadily. After ten steps, the variance is ten. After one hundred steps, the variance is one hundred. After one thousand steps, the variance is one thousand. This is linear growth - the variance increases at a constant rate with the number of steps.

Before we prove why this is true, let us remind ourselves what variance means and why we care about it. Variance is a measure of spread or dispersion. It quantifies how spread out the possible values of a random variable are around its expected value. A small variance means the values cluster tightly around the mean. A large variance means the values are widely dispersed.

**Formal Definition of Variance**

The variance of a random variable Y is defined mathematically as Var(Y) = E[(Y - E[Y])²]. This formula says: take the random variable, subtract its expected value to get the deviation from the mean, square that deviation to make it positive, and then take the expected value of the squared deviation. The squaring serves two purposes: it makes negative and positive deviations count equally (both contribute positively to variance), and it gives more weight to large deviations.

There is an alternative formula for variance that is often easier to compute: Var(Y) = E[Y²] - (E[Y])². This says that variance equals the expected value of the square minus the square of the expected value. We will use this formula to compute the variance of our random walk.

**Computing Variance of a Single Step**

Let us start by computing the variance of one step Xᵢ. We already know that E[Xᵢ] = 0, so the alternative formula simplifies to Var(Xᵢ) = E[Xᵢ²] - 0 = E[Xᵢ²]. Now we need E[Xᵢ²], the expected value of the square of the step.

The step Xᵢ can equal plus one or minus one, each with probability one-half. When we square these, we get Xᵢ² equals one in both cases, because (+1)² = 1 and (-1)² = 1. Therefore, E[Xᵢ²] = (1/2)(1) + (1/2)(1) = 1/2 + 1/2 = 1. The expected value of the squared step is one.

Thus, Var(Xᵢ) = 1 - 0 = 1. Each step has variance one. This makes sense intuitively - each step moves you one unit away from where you are (either plus one or minus one), so the "typical" squared deviation is one, and the variance is one.

**Computing Variance of the Sum: Why Independence Matters**

Now we need to compute the variance of Sₙ = X₁ + X₂ + ... + Xₙ. Unlike expectation, variance does not always distribute nicely over sums. The rule for variance of a sum depends crucially on whether the random variables are independent.

For independent random variables, we have the fundamental rule: Var(X₁ + X₂ + ... + Xₙ) = Var(X₁) + Var(X₂) + ... + Var(Xₙ). The variance of a sum of independent random variables equals the sum of their variances. This is a beautiful and powerful fact, but it requires independence. If the variables are dependent, the rule can fail, sometimes dramatically.

In our random walk, the steps X₁, X₂, ..., Xₙ are independent by construction. Each coin flip does not know about the others. Each step is a fresh, independent random choice. Therefore, we can apply the rule: Var(Sₙ) = Var(X₁) + Var(X₂) + ... + Var(Xₙ) = 1 + 1 + ... + 1 = n. The variance of the position after n steps is exactly n.

**The Critical Subtlety: Variance versus Standard Deviation**

We have now established that the variance grows linearly with time - Var(Sₙ) = n. This is an important mathematical fact, but there is a subtlety that we must understand to interpret this correctly. Variance is measured in squared units, not in the original units. If we measure positions in steps, then variance is measured in steps squared. What does "one hundred steps squared" mean intuitively? It is hard to visualize or feel.

The measure that corresponds to our intuitive sense of "how far away" is not variance but standard deviation. The standard deviation is defined as the square root of the variance: σ(Y) = √(Var(Y)). Standard deviation has the same units as the original random variable, so it is interpretable as a typical distance.

For our random walk, the standard deviation after n steps is σ(Sₙ) = √(Var(Sₙ)) = √n. This is the key relationship: while variance grows linearly with time, standard deviation grows with the square root of time. This square root relationship is one of the most important and counterintuitive features of random walks and diffusive processes.

**Understanding Square Root Growth with Concrete Numbers**

Let us see what this square root growth means by computing specific examples. After one step, the variance is one, so the standard deviation is √1 = 1. After four steps, the variance is four, so the standard deviation is √4 = 2. After nine steps, the variance is nine, so the standard deviation is √9 = 3. After sixteen steps, the variance is sixteen, so the standard deviation is √16 = 4. After one hundred steps, the variance is one hundred, so the standard deviation is √100 = 10.

Now observe something remarkable. To double the standard deviation from one to two, the time must increase from one step to four steps - a factor of four. To double it again from two to four, the time must increase from four steps to sixteen steps - another factor of four. To double the standard deviation from ten to twenty, the time must increase from one hundred steps to four hundred steps - yet again, a factor of four. Every time you want to double the typical distance, you must quadruple the time. This is the signature of square root growth.

**The Contrast: Linear Growth versus Square Root Growth**

To appreciate how unusual square root growth is, let us contrast it with linear growth. If the typical distance grew linearly with time, then after ten steps you would typically be ten steps away from the origin. After one hundred steps, you would typically be one hundred steps away. After one thousand steps, you would typically be one thousand steps away. There would be a direct, proportional relationship: multiply the number of steps by ten, and you multiply the typical distance by ten.

But in a random walk, the relationship is dramatically different. After ten steps, the typical distance is about √10 ≈ 3.16 steps. After one hundred steps, the typical distance is √100 = 10 steps. After one thousand steps, the typical distance is √1000 ≈ 31.6 steps. When you multiplied the time by ten (from ten to one hundred steps), you only multiplied the typical distance by √10 ≈ 3.16 (from 3.16 to 10). When you multiplied the time by one hundred (from ten to one thousand steps), you only multiplied the distance by √100 = 10 (from 3.16 to 31.6). The spreading is much, much slower than linear.

**Why Does This Happen? The Cancellation Effect**

Why does a random walk spread so slowly? The answer lies in cancellation. When you take one hundred steps, you might go right twenty-five times and left twenty-five times, returning exactly to where you started. Or you might go right forty times and left sixty times, ending up twenty steps to the left. Or you might go right seventy times and left thirty times, ending up forty steps to the right. The point is that the individual steps partially cancel each other out. You take many steps, but the net progress is much smaller than the total distance walked.

Think of it like this: imagine you are walking randomly in a large empty field. You walk north, then east, then south, then west, then north again, and so on. You are walking a lot - you accumulate steps - but you keep doubling back on yourself. The total distance you walk (the sum of the lengths of all your steps) grows linearly with time. But your displacement from the starting point (the straight-line distance from where you are now to where you started) grows much more slowly, with the square root of time, because the steps cancel each other out.

**Making It Visceral: A Numerical Example**

Suppose you walk ten thousand steps in a random walk. You might initially expect that after ten thousand steps, you would be far from the origin - perhaps thousands of steps away. But the typical distance is only √10000 = 100 steps. You walked ten thousand steps but only made net progress of about one hundred steps. The cancellation factor is about one hundred. If you continue to one million steps, the typical distance is √1000000 = 1000 steps. You walked a million steps but only got about a thousand steps away. The cancellation factor is now one thousand.

This slow spreading is not a bug or a curiosity - it is the essential nature of random, undirected motion. It is why diffusion is slow, why heat spreads gradually, why smoke from a candle takes time to fill a room. Anything that moves randomly spreads at a rate proportional to the square root of time, not to time itself.

**Why Not Slower or Faster? The Special Nature of Square Root Growth**

The text notes that the growth is neither zero (bounded) nor linear (or faster). Let us understand why square root growth is the natural middle ground. If the typical distance stayed bounded - did not grow at all - then the random walk would just jiggle around in a small neighborhood of the origin forever. It would never explore the full number line. This would happen if the steps were not independent but instead pulled the walk back toward the origin. That is not the case for a simple random walk.

On the other extreme, if the typical distance grew linearly or faster, the walk would race away from the origin. After enough time, it would be at enormous distances, and the probability of ever returning near the origin would vanish. This would happen if there were a drift - a tendency to move in one direction. But in a symmetric random walk, there is no drift. The walk has no preferred direction.

Square root growth is what emerges naturally when motion is random and undirected. The walk explores the line, spreading out to larger and larger distances, but slowly and hesitatingly because of the constant cancellation of steps. It is the growth rate of pure diffusion without drift.

**Property Three: The Distribution Approaches Normal**

**Statement of the Property and Why Shape Matters**

The third property concerns the shape of the probability distribution of the position. While the first two properties told us about the center (expected value zero) and spread (variance n) of the distribution, the third property tells us about its shape - the pattern of probabilities across all possible positions. The property states that as n grows large, the distribution of Sₙ approaches a normal (Gaussian) distribution with mean zero and variance n.

Before we delve into what this means and why it is true, we must build up our understanding carefully from the foundations. We will need to understand what a probability distribution is, what we mean by "shape," what values are even possible, how to count the ways to reach each value, and finally why this all converges to a bell curve. This will require patience and detail, but it is worth it - this property is central to everything that follows.

**Reminder: What Is a Probability Distribution?**

Let us start by making sure we understand exactly what we mean by a probability distribution. A probability distribution is a complete description of the randomness of a random variable. It tells us, for every possible value the variable could take, what the probability is of getting that value. If we know the distribution, we can answer any probabilistic question about the variable.

For a discrete random variable like Sₙ (which can only take specific integer values), the distribution is given by a list of probabilities. We write P(Sₙ = k) to mean "the probability that Sₙ equals k." If we list out P(Sₙ = k) for every possible value of k, we have completely specified the distribution. We can plot this as a bar chart, with k on the horizontal axis and P(Sₙ = k) on the vertical axis. The shape of this bar chart is what we mean by the "shape" of the distribution.

**Understanding the Sample Space: What Positions Are Possible?**

Now let us understand what values Sₙ can actually take. This is called the sample space - the set of all possible outcomes. For a random walk, the sample space depends on n, the number of steps taken. Let us build this up from the beginning to see the pattern clearly.

After zero steps, we are at position S₀ = 0. There is only one possible position, and we are there with probability one (certainty). The sample space is just the set {0}.

After one step, we can be at position +1 (if we stepped right) or -1 (if we stepped left). The sample space is {-1, +1}. Notice that we cannot be at position 0 after one step - that is not reachable in a single step from the origin.

After two steps, let us think carefully. We took two steps, each either plus one or minus one. What are the possible net results? If both steps were right, we end at +2. If both were left, we end at -2. If one was right and one was left, they cancel out and we end at 0. So the sample space is {-2, 0, +2}. Notice that we cannot be at +1 or -1 after two steps. Why not? Because after an even number of steps, the position must be even. Each step changes position by one unit. After two steps, we have changed position by two units in total (though they might cancel). The only way to end at an odd position would be if we took an odd number of steps.

After three steps, the sample space is {-3, -1, +1, +3}. After four steps, it is {-4, -2, 0, +2, +4}. Do you see the pattern? After n steps, we can be at any position from -n to +n, but only at positions that have the same parity as n. If n is even, only even positions are reachable. If n is odd, only odd positions are reachable. The positions are spaced two units apart, and there are n+1 possible positions in total.

This parity constraint is important. It means the sample space is not every integer between -n and +n, but rather every other integer. When we draw the probability distribution, we will have bars only at these specific positions, with gaps of two units between them.

**Counting Paths: How to Compute Probabilities**

Now comes the key question: for a given position k in the sample space, what is the probability of ending there after n steps? To answer this, we use a technique called counting paths or counting sequences. The idea is to count how many different sequences of coin flips lead to position k, and then use the fact that each sequence has the same probability.

Let us think about what it takes to end at position k after n steps. The position is the sum of all the steps: Sₙ = X₁ + X₂ + ... + Xₙ. Each Xᵢ is either +1 or -1. If we end at position k, that means the net result is k. How can we get a net result of k? We need some number of +1 steps and some number of -1 steps, such that they add up to k.

Let us say we take r steps to the right (each contributing +1) and ℓ steps to the left (each contributing -1). Then we need r + ℓ = n (the total number of steps) and r - ℓ = k (the net position). We can solve these two equations. Adding them gives 2r = n + k, so r = (n+k)/2. Subtracting gives 2ℓ = n - k, so ℓ = (n-k)/2. Notice that for these to be whole numbers, n and k must have the same parity - which we already knew from the sample space analysis.

So to reach position k after n steps, we need exactly (n+k)/2 steps to the right and (n-k)/2 steps to the left. Now the question becomes: in how many different ways can we choose which of the n steps are right steps? This is a combinatorial question. We are choosing (n+k)/2 items from a set of n items. The number of ways to do this is given by the binomial coefficient, written as C(n, (n+k)/2) or "n choose (n+k)/2."

The binomial coefficient C(n, m) equals n! / (m! (n-m)!), where the exclamation mark denotes factorial. For example, C(4, 2) = 4! / (2! 2!) = (4×3×2×1) / ((2×1)(2×1)) = 24 / 4 = 6. There are six ways to choose which two of four steps are right steps.

Now, each specific sequence of n coin flips has probability (1/2)ⁿ, because each flip is heads or tails with probability 1/2 independently. There are C(n, (n+k)/2) sequences that lead to position k, and each has probability (1/2)ⁿ. Therefore, the total probability of ending at position k is:

P(Sₙ = k) = C(n, (n+k)/2) × (1/2)ⁿ

This formula allows us to compute the exact probability of any position after any number of steps. Let us see it in action with concrete examples.

**A Detailed Example: After Two Steps**

Let us work through the case of n = 2 in complete detail to see how everything fits together. After two steps, the sample space is {-2, 0, +2}. Let us compute P(S₂ = k) for each value of k.

**Case 1: Position +2**

To reach position +2, we need (2+2)/2 = 2 steps to the right and (2-2)/2 = 0 steps to the left. In other words, both steps must be right steps. How many ways are there to choose which two steps out of two are right steps? Only one way - both of them. So C(2, 2) = 1.

The probability is P(S₂ = +2) = C(2, 2) × (1/2)² = 1 × 1/4 = 1/4.

Let us verify this by listing all sequences. With two flips, the possible sequences are: HH, HT, TH, TT (where H means heads/right and T means tails/left). Only one sequence, HH, leads to position +2. There are four sequences total, so the probability is 1/4. Correct.

**Case 2: Position -2**

To reach position -2, we need (2-2)/2 = 0 steps to the right and (2+2)/2 = 2 steps to the left. Both steps must be left steps. There is only one way to choose zero steps out of two to be right steps (equivalently, all steps are left). So C(2, 0) = 1.

The probability is P(S₂ = -2) = C(2, 0) × (1/2)² = 1 × 1/4 = 1/4.

Verifying: only the sequence TT leads to position -2. Probability is 1/4. Correct.

**Case 3: Position 0**

To reach position 0, we need (2+0)/2 = 1 step to the right and (2-0)/2 = 1 step to the left. We need to choose which one of the two steps is a right step. There are two ways: the first step could be right (sequence HT), or the second step could be right (sequence TH). So C(2, 1) = 2.

The probability is P(S₂ = 0) = C(2, 1) × (1/2)² = 2 × 1/4 = 2/4 = 1/2.

Verifying: sequences HT and TH both lead to position 0. Two out of four sequences, so probability is 2/4 = 1/2. Correct.

So the complete distribution after two steps is:
- P(S₂ = -2) = 1/4
- P(S₂ = 0) = 1/2  
- P(S₂ = +2) = 1/4

Notice that these probabilities sum to one, as they must (something must happen). If we plot this as a bar chart, we see a peak in the middle at 0 (with height 1/2) and two shorter bars on either side at -2 and +2 (each with height 1/4). This is the shape of the distribution. It is symmetric around zero, which makes sense given the symmetry of the random walk.

**How the Shape Evolves as n Grows**

Let us now see what happens as we take more and more steps. After three steps, the sample space is {-3, -1, +1, +3}. Let us compute the probabilities.

- P(S₃ = -3) = C(3, 0) × (1/2)³ = 1 × 1/8 = 1/8 (all three steps left)
- P(S₃ = -1) = C(3, 1) × (1/2)³ = 3 × 1/8 = 3/8 (one step right, two left)
- P(S₃ = +1) = C(3, 2) × (1/2)³ = 3 × 1/8 = 3/8 (two steps right, one left)
- P(S₃ = +3) = C(3, 3) × (1/2)³ = 1 × 1/8 = 1/8 (all three steps right)

The distribution is again symmetric, peaked in the middle (the middle values -1 and +1 each have probability 3/8), with lower probabilities at the extremes.

After four steps, the sample space is {-4, -2, 0, +2, +4} and the probabilities are:

- P(S₄ = -4) = C(4, 0) × (1/2)⁴ = 1 × 1/16 = 1/16
- P(S₄ = -2) = C(4, 1) × (1/2)⁴ = 4 × 1/16 = 4/16
- P(S₄ = 0) = C(4, 2) × (1/2)⁴ = 6 × 1/16 = 6/16
- P(S₄ = +2) = C(4, 3) × (1/2)⁴ = 4 × 1/16 = 4/16
- P(S₄ = +4) = C(4, 4) × (1/2)⁴ = 1 × 1/16 = 1/16

Notice the pattern in the binomial coefficients: 1, 4, 6, 4, 1. These are the numbers from the fourth row of Pascal's triangle. The distribution is strongly peaked at the center (position 0 has probability 6/16, nearly 40%), with probabilities tapering off symmetrically toward the extremes.

As n continues to increase, several things happen. First, the number of possible positions grows - there are n+1 of them. Second, the probabilities become smaller for each individual position, because they must sum to one and there are more positions to share the probability among. Third, and most importantly for our purposes, the shape traced out by the bars starts to look smoother and more like a continuous curve.

By the time n reaches twenty or thirty, if you plot the bars of the distribution and draw a smooth curve connecting their tops, that curve looks remarkably like a bell - the famous bell curve of the normal distribution. By n equal to one hundred, the resemblance is so close that the discrete bars are almost indistinguishable from a continuous normal curve unless you look very carefully.

**What Is a Normal Distribution? A Reminder**

Before we can appreciate the convergence to normality, we must understand what a normal distribution is. The normal distribution, also called the Gaussian distribution after the mathematician Carl Friedrich Gauss, is a specific continuous probability distribution. It is defined by a probability density function that has the shape of a symmetric bell curve.

The normal distribution is completely characterized by two parameters: the mean μ (mu), which specifies the center of the distribution, and the variance σ² (sigma squared), which specifies the spread. We denote a normal distribution with mean μ and variance σ² as N(μ, σ²). The standard normal distribution is N(0, 1) - mean zero and variance one.

The probability density function of a normal distribution with mean μ and variance σ² is:

f(x) = (1 / √(2πσ²)) × exp(-(x-μ)² / (2σ²))

Do not worry if this formula looks complicated - the key point is that it produces a symmetric bell-shaped curve, peaked at x = μ, with the width of the bell determined by σ. The larger σ is, the wider and flatter the bell. The smaller σ is, the taller and narrower the bell.

The normal distribution has several special properties that make it extremely important in probability theory and statistics. It is symmetric. It is unimodal (has only one peak). About 68% of the probability mass lies within one standard deviation of the mean, about 95% within two standard deviations, and about 99.7% within three standard deviations. These are called the empirical rules or the 68-95-99.7 rule.

**The Central Limit Theorem: Why Normality Emerges**

Now we come to the heart of the matter: why does the distribution of Sₙ approach a normal distribution as n grows? This is not a coincidence or a curiosity specific to random walks. It is a manifestation of one of the most profound and powerful results in all of probability theory, the Central Limit Theorem.

The Central Limit Theorem states, roughly speaking, that when you add up many independent random variables, the distribution of the sum approaches a normal distribution, regardless of what the distributions of the individual variables look like. The individual variables do not need to be normal. They do not even need to have the same distribution (though certain technical conditions must be met). As long as they are independent and their variances are not too wildly different, the sum will be approximately normal for large n.

In our case, Sₙ = X₁ + X₂ + ... + Xₙ is the sum of n independent random steps. Each step Xᵢ has a very simple, very non-normal distribution - it takes only two values, +1 with probability 1/2 and -1 with probability 1/2. This distribution is as far from a bell curve as you can imagine. It is discrete, symmetric, but concentrated on just two points with a huge gap in between.

And yet, when we add up many such steps, something magical happens. The distribution of the sum smooths out, spreads out, and takes on the shape of a bell curve. The discrete jumps average out into something smooth. The extreme concentration on two points spreads into a continuous distribution over many points. The Central Limit Theorem tells us this must happen, and our explicit calculation of the probabilities confirms it.

Why does this happen? The intuition is that when many independent random influences combine, the extreme outcomes (where all or most steps go in the same direction) become very rare because they require a very specific pattern of coin flips. The moderate outcomes (where roughly half go each direction, with some net imbalance) are much more common because there are many, many different patterns that lead to them. The binomial coefficients capture exactly this - the middle terms are much larger than the extreme terms. And as n grows, this concentration in the middle becomes more and more pronounced, while simultaneously the scale spreads out, creating the bell shape.

**How Good Is the Approximation?**

The statement that the distribution "approaches" normal means that the approximation gets better and better as n increases, and becomes exact in the limit as n approaches infinity. But how fast does this happen? How large does n need to be before we can treat the distribution as approximately normal?

The answer depends on how accurate we need to be, but as a rule of thumb, the approximation is quite good already by n equal to thirty or so. By n equal to one hundred, the discrete distribution is nearly indistinguishable from a continuous normal curve for most practical purposes. By n equal to one thousand, the agreement is essentially perfect unless you need extremely high precision.

There is a more precise way to state the convergence using the idea of standardization. Define the standardized position as Zₙ = Sₙ / √n. This divides the position by its standard deviation (recall that the standard deviation of Sₙ is √n). The standardized position has mean zero and variance one. The Central Limit Theorem tells us that as n approaches infinity, the distribution of Zₙ converges to the standard normal distribution N(0, 1).

This convergence can be made precise in various mathematical senses. The cumulative distribution functions converge pointwise. The probability density functions (if we smooth out the discrete bars) converge uniformly. The characteristic functions converge. All of these are ways of saying that the distribution gets closer and closer to normal in every meaningful sense.

**Why This Property Is Crucial for Finance**

The convergence to normality is perhaps the most important property of random walks for applications in finance. Why? Because Brownian motion, the continuous-time limit of random walks, is defined to have exactly normal increments at every time scale. When we construct Brownian motion by taking the limit of finer and finer random walks (which we will do later in this project), the property of approaching normality will become the property of being exactly normal.

In continuous time, Brownian motion W(t) is defined such that for any time interval from s to t, the increment W(t) - W(s) follows a normal distribution with mean zero and variance t - s. This is not an approximation - it is exact by definition. The random walk teaches us to expect this. We see that as we take more steps, the distribution becomes more normal. In the limit of infinitely many infinitesimally small steps - which is Brownian motion - the distribution is perfectly normal.

Moreover, in the Black-Scholes model and most of quantitative finance, we rely heavily on the assumption that log returns or price changes are normally distributed. This assumption is justified precisely because price changes are the sum of many small, independent random influences - news, trades, sentiment shifts, and so on. The Central Limit Theorem guarantees that such sums will be approximately normal, giving us a theoretical foundation for the models we use to price options, manage risk, and construct portfolios.

Without the normality, we would not have the elegant closed-form solutions that make quantitative finance practical. The normal distribution has special properties (like being closed under addition, having explicit formulas for probabilities, being fully characterized by two parameters) that make calculations tractable. Other distributions would make the mathematics far more difficult or impossible.

**Property Four: Independent Increments and the Markov Property**

**Statement of the Property and Why Memory Matters**

The fourth property concerns the relationship between the position of the walk at different times. We have already stated that the individual steps X₁, X₂, X₃, and so on are independent - each coin flip does not know about the previous flips. But there is a slightly more general and more powerful way to state this independence that will be crucial when we move to continuous time. This is the property of independent increments, which is closely related to the Markov property.

These properties tell us something profound about the random walk: it has no memory. The future depends only on where we are now, not on how we got here. This may sound like a technical detail, but it is actually one of the most important and useful properties of the random walk. It is what allows us to compute probability distributions for future positions, to make predictions, and ultimately to price financial derivatives. Let us understand exactly what this means and why it matters so much.

**What Is an Increment? Building the Concept Carefully**

Before we can discuss independent increments, we must first understand what an increment is. The word "increment" means a change or a difference. In the context of a random walk, an increment is the change in position between two times.

Specifically, suppose we look at the random walk at time s and then later at time t, where s < t. At time s, the position is Sₛ. At time t, the position is Sₜ. The increment from time s to time t is defined as the difference:

Increment = Sₜ - Sₛ

This measures how much the position changed during the time interval from s to t. If we started at position five at time s and ended at position twelve at time t, the increment is twelve minus five, which equals seven. The walk moved seven steps to the right (net) during that interval. If we started at position three and ended at position minus two, the increment is minus two minus three, which equals minus five. The walk moved five steps to the left (net) during that interval.

We can express the increment in terms of the individual steps. Recall that Sₜ equals the sum of all steps from the beginning up to time t: Sₜ = X₁ + X₂ + ... + Xₜ. Similarly, Sₛ = X₁ + X₂ + ... + Xₛ. Therefore:

Sₜ - Sₛ = (X₁ + X₂ + ... + Xₜ) - (X₁ + X₂ + ... + Xₛ)

The steps X₁ through Xₛ appear in both sums and cancel out, leaving:

Sₜ - Sₛ = Xₛ₊₁ + Xₛ₊₂ + ... + Xₜ

So the increment is simply the sum of the steps taken between times s and t. If s equals five and t equals ten, then S₁₀ - S₅ = X₆ + X₇ + X₈ + X₉ + X₁₀. This is the net effect of the five steps taken during that time window.

**Reminder: What Does "Independent" Mean?**

Before we define independent increments, let us remind ourselves what independence means in probability. Two random variables X and Y are independent if knowing the value of one provides no information about the value of the other. More formally, for any values a and b, the probability that X equals a AND Y equals b must factor into the product:

P(X = a and Y = b) = P(X = a) × P(Y = b)

This is the defining property of independence. The joint probability equals the product of the marginal probabilities. Independence is a very strong condition - it means the variables are completely unrelated, with no correlation or influence between them whatsoever.

For example, if I flip two coins independently, knowing that the first coin landed heads tells me nothing about the second coin. The probability that the second coin is heads is still one-half, regardless of what the first coin showed. That is independence.

In contrast, if two variables are dependent, knowing one provides information about the other. If the temperature today is thirty degrees Celsius, that tells me something about tomorrow's temperature - it is likely to be relatively warm as well. Today's and tomorrow's temperatures are not independent; they are correlated.

**The Property of Independent Increments Defined**

Now we can state the property of independent increments precisely. The property says that increments over non-overlapping time intervals are independent. More formally, suppose we take several time intervals [s₁, t₁], [s₂, t₂], [s₃, t₃], and so on, where the intervals do not overlap. This means that each interval ends before the next one begins: t₁ ≤ s₂, t₂ ≤ s₃, and so on. Then the increments during these intervals are mutually independent:

Sₜ₁ - Sₛ₁, Sₜ₂ - Sₛ₂, Sₜ₃ - Sₛ₃, ... are independent random variables.

Intuitively, this says that what happens in one time interval does not affect what happens in a later, non-overlapping interval. If I watch the walk from time zero to time ten, and you watch the walk from time eleven to time twenty, what I observe provides no information about what you will observe. The future increments depend only on where the walk is now, not on how it got there.

**Why This Is True for the Random Walk: The Mathematical Reason**

Why does the random walk have independent increments? The reason comes directly from the independence of the individual steps. Consider the increment from time s to time t:

Sₜ - Sₛ = Xₛ₊₁ + Xₛ₊₂ + ... + Xₜ

This increment is a function only of the steps from s+1 to t. These steps are independent of all the steps from time one to time s by the construction of the random walk - each coin flip is independent of all previous flips. Therefore, the increment Sₜ - Sₛ, being a function of steps s+1 through t, is independent of the entire history up to time s, which depends only on steps one through s.

Similarly, if we have two non-overlapping intervals [s₁, t₁] and [s₂, t₂] with t₁ ≤ s₂, the increment during the first interval depends on steps s₁+1 through t₁, while the increment during the second interval depends on steps s₂+1 through t₂. These are disjoint sets of steps, and since the steps are all mutually independent, the increments are independent.

This independence is powerful and important. It means the walk has no memory in a very precise sense. What happened in the past does not influence what will happen in the future, except through the current position.

**The Markov Property: A Stronger Statement of Memorylessness**

There is a related property called the Markov property that is slightly stronger but very closely connected to independent increments. A stochastic process has the Markov property if the future depends on the past only through the present state. For the random walk, this means that to predict the probabilities for all future positions, you only need to know the current position Sₙ. Knowing the entire history S₀, S₁, S₂, ..., Sₙ₋₁ of how the walk arrived at Sₙ provides no additional predictive power beyond knowing Sₙ itself.

The Markov property is sometimes stated as: "Given the present, the future is independent of the past." This is a memorable way to capture the essence of memorylessness. Once you know where you are now, it does not matter how you got there - the future probabilities are the same regardless of the path taken.

For the random walk, both the Markov property and independent increments hold. These properties are enormously useful for analysis because they mean we can summarize the entire state of the system with a single number - the current position. We do not need to track the entire path history, which would be vastly more complicated. This simplification is what makes many calculations tractable.

**The Critical Question: How Can We Know the Future Distribution?**

Now we come to the heart of why this property matters so much. Let us pose a concrete question. Suppose you tell me that the random walk is currently at position minus seven. You then ask me: what is the probability distribution of the position after ten more steps? Can I answer this question? If so, how? And what role does the Markov property play?

Before the Markov property, we might think this question is impossible to answer without more information. After all, there are many different ways to arrive at position minus seven. Maybe the walk got there by drifting steadily downward over many steps. Maybe it jumped up to plus twenty and then crashed down. Maybe it oscillated wildly. Does the path history matter for predicting the future? This is where the Markov property shows its power.

**What "Knowing the Distribution" Means**

First, let us be clear about what we are trying to know. When I say I know the probability distribution of the position after ten more steps, I mean I can answer questions like: What is the probability that the position will be three? What is the probability it will be minus eleven? What is the probability it will be any particular value? I can draw the complete bar chart of probabilities and tell you exactly how likely each outcome is. This is complete probabilistic knowledge about the future position.

**How the Markov Property Allows Us to Compute the Distribution**

Here is the key insight. Because the random walk has the Markov property, the ten future steps are independent of everything that happened before now. Each of the ten steps will be plus one or minus one with probability one-half, exactly as if we were starting a fresh random walk from scratch. The fact that we are currently at position minus seven does not influence how the future steps behave at all.

This means we can think about the problem in a very simple way. We are at minus seven now. The next ten steps will add some random displacement to our current position. What is the distribution of that displacement? It is exactly the distribution of a random walk that starts at zero and takes ten steps. We already know that distribution from the theory we studied - the position after ten steps is distributed with mean zero and variance ten, and we can compute the probability of each value using the binomial coefficients.

The final position will be our current position minus seven plus the displacement from the ten steps. So if the displacement is plus four, we end at minus three. If the displacement is minus two, we end at minus nine. Since we know the distribution of the displacement, we can compute the distribution of the final position - it is simply the displacement distribution, shifted by minus seven.

**A Concrete Numerical Example: Computing Specific Probabilities**

Let us be completely concrete with numbers to see how this works in practice. I am at position minus seven. What is the probability that after ten more steps, I will be at position plus three?

To go from minus seven to plus three, I need a net displacement of plus ten. That means the ten future steps must sum to plus ten. For a sum of ten steps to equal plus ten, all ten steps must be plus one (right). There is no other way - even one minus one step would make the sum less than ten. The probability that all ten steps are plus one is (1/2)¹⁰, which equals one over one thousand twenty-four. So:

P(S₁₀ = +3 | currently at -7) = 1/1024 ≈ 0.098%

This is a very small probability, which makes sense - getting all ten steps to go in the same direction is rare.

What is the probability that I will be at position minus five? To go from minus seven to minus five, I need a net displacement of plus two. For ten steps to sum to plus two, I need six steps of plus one and four steps of minus one. Six plus four equals ten steps total (correct), and six minus four equals two net displacement (correct).

How many ways are there to choose which six of the ten steps are plus one? This is the binomial coefficient C(10, 6), which equals ten factorial divided by six factorial times four factorial, which equals two hundred ten. Each specific arrangement of six plus ones and four minus ones has probability (1/2)¹⁰. Therefore:

P(S₁₀ = -5 | currently at -7) = C(10, 6) × (1/2)¹⁰ = 210/1024 ≈ 20.5%

This is the highest probability among all possible positions, because minus five is closest to the expected final position of minus seven plus zero equals minus seven (since the expected displacement is zero).

**The General Formula: A Powerful Tool**

More generally, if I am currently at position x and I want to know the probability of being at position y after n more steps, I need a displacement of y minus x. The probability of that displacement is:

P(position y after n steps | currently at x) = P(displacement of y-x in n steps) = C(n, (n+(y-x))/2) × (1/2)ⁿ

This formula works for any starting position x, any target position y, and any number of steps n (as long as y-x and n have the same parity). This is the power of the Markov property - we have a universal formula that does not depend on the history, only on where we are now and where we want to go.

**What Would Happen Without the Markov Property?**

To truly appreciate the power of the Markov property, let us imagine what would happen if the random walk did not have this property. Suppose instead that the walk had memory - specifically, imagine that if the previous step was plus one, then the next step is plus one with probability seventy percent and minus one with probability thirty percent. But if the previous step was minus one, then the next step is plus one with probability thirty percent and minus one with probability seventy percent. The walk has a tendency to continue in the direction it recently moved.

Now suppose you tell me the walk is at position minus seven and ask me for the probability distribution after ten more steps. Can I answer this with just the information that the current position is minus seven? No, I cannot. I need to know how the walk arrived at minus seven because that determines the probabilities for the next step.

If the walk reached minus seven through a sequence of recent downward steps, then the next step is likely to also be downward (seventy percent probability). The walk has momentum. But if the walk reached minus seven by first going up to plus twenty and then dropping sharply, the most recent step was probably downward, so again the next step is likely downward. But if the walk oscillated around minus seven for a while, the recent steps could have been mixed, and the probabilities would be different.

The path history matters. To predict the future, I need to know not just the current position but also the recent history, or perhaps the entire history. The distribution of future positions depends on the specific path that led to the current position. This makes the analysis vastly more complicated. Instead of one universal formula, I would need different formulas for different histories. The state of the system is no longer just a single number (position) but an entire path or at least several recent steps.

**A Comparison Example: Two Paths to the Same Position**

Let us make this even more concrete. Imagine two people, Alice and Bob, both doing random walks. Alice has taken one hundred steps and arrived at position minus seven. Bob has taken only twenty steps and also arrived at position minus seven. They are at the same position right now, but they took very different paths to get there.

Now you ask: who is more likely to be at position plus three after ten more steps? With the Markov property, the answer is that they have exactly the same probability. The fact that Alice took one hundred steps versus Bob's twenty is irrelevant. All that matters is that both are currently at minus seven. From that starting point, the next ten steps behave identically for both of them - each step is plus one or minus one with probability one-half, independent of anything that happened before. The probability that either Alice or Bob ends at plus three is the same: one over one thousand twenty-four.

This is what "the walk has no memory" means. The past is completely forgotten. Only the present position matters for predicting the future. And this is what makes calculation simple - we have one answer that works for everyone at position minus seven, regardless of their history.

Without the Markov property, Alice and Bob might have different probabilities even though they are at the same position, because their paths to that position were different. We would need to track and account for those differences, making everything much more complicated.

**Why This Property Is Essential for Financial Modeling**

In the context of financial modeling, the Markov property (or something close to it) is crucial. It says that the current price of a stock contains all the relevant information for predicting future prices. You do not need to know the entire price history - whether the stock got to its current price by rising steadily, or by spiking and crashing, or by oscillating. All that matters is where the price is now.

This is related to the concept of market efficiency. In an efficient market, all available information is already incorporated into the current price. The history of how the price evolved is already "priced in." Therefore, knowing that history provides no additional predictive power beyond knowing the current price. This is essentially a Markov property applied to markets.

Of course, in reality, markets may not be perfectly Markovian. There may be momentum effects, where recent price movements influence future movements. There may be mean reversion, where prices that have risen a lot tend to fall back. But the Markov property is an excellent first approximation that makes models tractable. Most quantitative finance models, including Black-Scholes, assume a Markov property for the underlying price process.

**Connection to Option Pricing: A Preview**

There is a deep connection between the Markov property and the ability to price options using dynamic replication strategies. In the Black-Scholes framework, we continuously rebalance a portfolio of stock and bonds to replicate the payoff of an option. At each moment, we decide how much stock and how much bonds to hold based on the current stock price and the time remaining until expiration. We do not need to know the entire price history - only the current price and time. This is possible precisely because the underlying price process is Markovian. If it were not, replication would require tracking the entire history, which would be impractical or impossible.

**The Independence of Increments: A Slightly Different Perspective**

We have focused on the Markov property, but the closely related property of independent increments is also worth emphasizing. Independent increments says that what happens in one time interval is independent of what happens in a non-overlapping interval. This is particularly important for analyzing multiple time periods or comparing different time windows.

For example, suppose I want to know the joint probability that the walk is at position five after ten steps AND at position twelve after twenty steps. With independent increments, I can break this down: the probability of being at five after ten steps is one thing, and then independently, the probability of moving from five to twelve in the next ten steps is another thing. These two events are independent, so the joint probability is the product of the individual probabilities. Without independent increments, I would need to account for the correlation between the two time periods, which would be much harder.

**Summary of Why Property Four Matters**

The Markov property and independent increments are not just technical details. They are fundamental features that make random walks and their continuous-time analogues tractable and useful for modeling. They allow us to:

- Compute future probability distributions knowing only the current position, not the entire history
- Use simple, universal formulas that do not depend on the path taken
- Model complex systems with a minimal state description (just the current position)
- Price financial derivatives using dynamic replication strategies
- Analyze multi-period problems by breaking them into independent pieces

Without these properties, stochastic processes would be far more complicated to work with, and many of the elegant results in probability theory and quantitative finance would not exist. When we move to Brownian motion in continuous time, these properties will remain central. Brownian motion is defined to have independent increments and to be a Markov process. Everything we have learned about these properties in the discrete setting will carry over to the continuous setting, where they become even more powerful and widely applicable.

The random walk is teaching us not just mathematical facts but also a way of thinking about random evolution over time. The present contains all relevant information about the future. The past matters only insofar as it determines the present. This philosophical insight has implications far beyond mathematics, touching on how we understand causality, prediction, and the flow of time in stochastic systems.