from faker import Faker
from itertools import product
import mmh3

fake = Faker()

BLOOM_ARRAY_SIZES = [50, 250, 500]
FUNCTION_AMOUNT_SIZES = [3, 6, 9]
SPAM_LIST_SIZES = [50, 180, 350]
REAL_EMAILS_LIST_SIZES = [200, 500, 1000]

combinations = list(product(BLOOM_ARRAY_SIZES, FUNCTION_AMOUNT_SIZES, SPAM_LIST_SIZES, REAL_EMAILS_LIST_SIZES))

def generate_functions(amount_of_functions, max_range):
	functions = []
	for i in range(amount_of_functions):
		functions.append(lambda x, seed=i: mmh3.hash(x, seed=seed) % max_range)
	return functions

def generate_emails(amount_of_emails):
	emails = []
	for _ in range(amount_of_emails):
		emails.append(fake.ascii_company_email())
	return emails

class BloomFilter:
	def __init__(self, bit_array_size, amount_of_functions, initial_spams):
		self.bit_array = [0] * bit_array_size
		self.functions = generate_functions(amount_of_functions, bit_array_size)
		for email in initial_spams:
			for function in self.functions:
				self.bit_array[function(email)] = 1

	def is_spam(self, x):
		return all(self.bit_array[function(x)] == 1 for function in self.functions)

max_spam_list_size = max(SPAM_LIST_SIZES)
max_real_list_size = max(REAL_EMAILS_LIST_SIZES)
master_spam_emails = generate_emails(max_spam_list_size)
master_real_emails = generate_emails(max_real_list_size)

results = []

for combination in combinations:
	bloom_array_size, function_amount, spam_list_size, real_emails_list_size = combination
	spam_emails = master_spam_emails[:spam_list_size]
	bloom_filter = BloomFilter(bloom_array_size, function_amount, spam_emails)
	wild_emails = master_real_emails[:real_emails_list_size]
	false_positives = sum(1 for email in wild_emails if bloom_filter.is_spam(email))
	results.append([bloom_array_size, function_amount, spam_list_size, real_emails_list_size, false_positives])

results.sort(key=lambda x: x[-1])
for result in results:
    print(result)
