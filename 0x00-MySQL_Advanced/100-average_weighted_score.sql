--  creates a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
	DECLARE weight_score FLOAT;
	SET weight_score = (
		SELECT SUM(score * weight) / SUM(weight) FROM users AS us
		JOIN corrections AS cor ON us.id = cor.user_id
		JOIN projects AS pro ON cor.project_id = pro.id
		WHERE us.id = user_id
	);
	UPDATE users SET average_score = weight_score WHERE id = user_id;
END$$
DELIMITER ;
