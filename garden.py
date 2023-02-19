import spacy

# Load the small English language model
nlp = spacy.load('en_core_web_sm')

# Define a list of garden path sentences to process
gardenpathSentences = [
    "The horse raced past the barn fell.",
    "The old man the boat.",
    "The chicken is ready to eat was burnt.",
    "The dog that chased the cat meowed.",
    "The soldier decided to desert his dessert in the desert."
]

# Iterate over the garden path sentences
for sentence in gardenpathSentences:
    # Process each sentence with the NLP pipeline
    doc = nlp(sentence)
    
    # Print out the tokens and named entities for each sentence
    print(f"""
          Sentence: {sentence}
          Tokens: {[token.text for token in doc]}
          Entities: {[entity.label_ for entity in doc.ents]}" 
          """)
          
# Get the explanation for the "FAC" entity label
entity_fac = spacy.explain("FAC")
print(entity_fac)
# Prints "Buildings, airports, highways, bridges, etc."

# Get the explanation for the "NORP" entity label
entity_norp = spacy.explain("NORP")
print(entity_norp)

# print out Nationalities or religious or political groups
"""
Entities looked up: "FAC" and "NORP"
- Entity "FAC" refers to buildings, airports, highways, bridges, etc. This entity makes sense in terms of the sentence "The horse raced past the barn fell." Here, "barn" can be considered as a building and thus is correctly recognized as a "FAC" entity by spaCy.
- Entity "NORP" refers to nationalities or religious or political groups. For example, "Spanish", "Christian", "Democratic". This entity makes sense in terms of the sentence "The dog that chased the cat meowed." Here, there is no "NORP" entity recognized by spaCy, which is expected since none of the tokens in this sentence refer to nationalities or religious or political groups.
"""


