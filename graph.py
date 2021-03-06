"""
[New York Social Diary](http://www.newyorksocialdiary.com/) provides a fascinating lens onto New York's socially well-to-do.  The data forms a natural social graph for New York's social elite.  Take a look at this page of a recent run-of-the-mill holiday party:

`http://www.newyorksocialdiary.com/party-pictures/2014/holiday-dinners-and-doers`

Besides the brand-name celebrities, you will notice the photos have carefully annotated captions labeling those that appear in the photos.  We can think of this as implicitly implying a social graph: there is a connection between two individuals if they appear in a picture together.

The first step is to fetch the data.  This comes in two phases.

The first step is to crawl the data.  We want photos from parties before December 1st, 2014.  Go to
`http://www.newyorksocialdiary.com/party-pictures`
to see a list of (party) pages.  For each party's page, grab all the captions.  *Hints*:

  1. Click on the on the index page and see how they change the url.  Use this to determine a strategy to get all the data.

  2. Notice that each party has a date on the index page.  Use python's `datetime.strptime` function to parse it.

  3. Some captions are not useful: they contain long narrative texts that explain the event.  Usually in two stage processes like this, it is better to keep more data in the first stage and then filter it out in the second stage.  This makes your work more reproducible.  It's usually faster to download more data than you need now than to have to redownload more data later.

Now that you have a list of all captions, you should probably save the data on disk so that you can quickly retrieve it.  Now comes the parsing part.

  1. Some captions are not useful: they contain long narrative texts that explain the event.  Try to find some heuristic rules to separate captions that are a list of names from those that are not.  A few heuristics include:
      - look for sentences (which have verbs) and as opposed to lists of nouns.  For example, [nltk does part of speech tagging](http://www.nltk.org/book/ch05.html) but it is a little slow.  There may also be heuristics that accomplish the same thing.
      - Look for commonly repeated threads (e.g. you might end up picking up the photo credtis).
      - Long captions are often not lists of people.  The cutoff is subjective so to be definitive, *let's set that cutoff at 250 characters*.

  2. You will want to separate the captions based on various forms of punctuation.  Try using `re.split`, which is more sophisticated than `string.split`.

  3. You might find a person named "ra Lebenthal".  There is no one by this name.  Can anyone spot what's happening here?

  4. This site is pretty formal and likes to say things like "Mayor Michael Bloomberg" after his election but "Michael Bloomberg" before his election.  Can you find other ('optional') titles that are being used?  They should probably be filtered out b/c they ultimately refer to the same person: "Michael Bloomberg."

For the analysis, we think of the problem in terms of a [network](http://en.wikipedia.org/wiki/Computer_network) or a [graph](http://en.wikipedia.org/wiki/Graph_%28mathematics%29).  Any time a pair of people appear in a photo together, that is considered a link.  What we have described is more appropriately called an (undirected) [multigraph](http://en.wikipedia.org/wiki/Multigraph) with no self-loops but this has an obvious analog in terms of an undirected [weighted graph](http://en.wikipedia.org/wiki/Graph_%28mathematics%29#Weighted_graph).  In this problem, we will analyze the social graph of the new york social elite.

For this problem, we recommend using python's `networkx` library.
"""

from lib import QuestionList, Question, StringNumberListValidateMixin, TupleListValidateMixin
QuestionList.set_name("graph")

@QuestionList.add
class Degree(StringNumberListValidateMixin, Question):
  """
  The simplest question you might want to ask is 'who is the most popular'?  The easiest way to answer this question is to look at how many connections everyone has.  Return the top 100 people and their degree.  Remember that if an edge of the graph has weight 2, it counts for 2 in the degree.
  """
  def solution(self):
    """
    A list of 100 tuples of (name, degree) in descending order of degree
    """
    return [('Alec Baldwin', 69)] * 100


@QuestionList.add
class PageRank(StringNumberListValidateMixin, Question):
  """
  A similar way to determine popularity is to look at their [pagerank](http://en.wikipedia.org/wiki/PageRank).  Pagerank is used for web ranking and was originally [patented](http://patft.uspto.gov/netacgi/nph-Parser?patentnumber=6285999) by Google and is essentially the [stationary distribution](http://en.wikipedia.org/wiki/Markov_chain#Stationary_distribution_relation_to_eigenvectors_and_simplices) of a [markov chain](http://en.wikipedia.org/wiki/Markov_chain) implied by the social graph.

  Use 0.85 as the damping parameter so that there is a 15% chance of jumping to another vertex.
  """
  def solution(self):
    """
    A list of 100 tuples of the form (name, pagerank) in descending order of pagerank
    """
    return [('Martha Stewart', 0.0002051725372886844)] * 100


@QuestionList.add
class BestFriends(TupleListValidateMixin, Question):
  """
  Another interesting question is who tend to co-occur with each other.  Give us the 100 edges with the highest weights

  Google these people and see what their connection is.  Can we use this to detect instances of infidelity?
  """
  def solution(self):
    """
    A list of 100 triples of the form (person1, person2, count) in descending order of count
    """
    return [(('David Lauren', 'Lauren Bush'), 19)] * 100

  def list_length(cls):
    return 100

  @classmethod
  def tuple_validators(cls):
    return (cls.validate_tuple, cls.validate_int)
