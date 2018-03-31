from calculation import StreetCreditScoreCalculator

def main():
	calculator = StreetCreditScoreCalculator()
	score = calculator.calculate()

	print("Total Score:", score.score)
	for category in score.category_scores:
		print("{}: {}".format(category.name, category.score))
		for metric_score in category.metric_scores:
			print("  {:4} {}".format(metric_score.score, metric_score.name))
			print("       {}".format(metric_score.description))

if __name__ == '__main__':
	main()