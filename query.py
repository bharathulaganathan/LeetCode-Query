import requests


def leetcode_query(query, variables=None):
    """
    Generic function to query LeetCode GraphQL API
    """

    LEETCODE_API_URL = "https://leetcode.com/graphql"

    headers = {
        'Content-Type': 'application/json',
    }

    payload = {
        'query': query,
        'variables': variables or {}
    }

    response = requests.post(
        LEETCODE_API_URL,
        json=payload,
        headers=headers
    )

    return response.json()


def questionOfToday():
    query = """
        query questionOfToday {
            activeDailyCodingChallengeQuestion {
                link
            }
        }
    """
    return leetcode_query(query)

def questionOfTodayV2():
    query = """
        query questionOfTodayV2 {
            activeDailyCodingChallengeQuestion {
                date
                userStatus
                link
                question {
                    id: questionId
                    titleSlug
                    title
                    translatedTitle
                    questionFrontendId
                    paidOnly: isPaidOnly
                    difficulty
                    topicTags {
                        name
                        slug
                        nameTranslated: translatedName
                    }
                    status
                    isInMyFavorites: isFavor
                    acRate
                    frequency: freqBar
                }
            }
        }
    """
    return leetcode_query(query)

def problemsetQuestionListV2(variables=None):
    query = """
        query problemsetQuestionListV2($filters: QuestionFilterInput, $limit: Int, $searchKeyword: String, $skip: Int, $sortBy: QuestionSortByInput, $categorySlug: String) {
            problemsetQuestionListV2(
                filters: $filters
                limit: $limit
                searchKeyword: $searchKeyword
                skip: $skip
                sortBy: $sortBy
                categorySlug: $categorySlug
            ) {
                questions {
                    id
                    titleSlug
                    title
                    translatedTitle
                    questionFrontendId
                    paidOnly
                    difficulty
                    topicTags {
                        name
                        slug
                        nameTranslated
                    }
                    status
                    isInMyFavorites
                    frequency
                    acRate
                    contestPoint
                }
                totalLength
                finishedLength
                hasMore
            }
        }
    """
    variables = variables or {}
    return leetcode_query(query, variables)

def questionDetail(titleSlug):
    query = """
        query questionDetail($titleSlug: String!) {
            languageList {
                id
                name
            }
            submittableLanguageList {
                id
                name
                verboseName
            }
            statusList {
                id
                name
            }
            questionDiscussionTopic(questionSlug: $titleSlug) {
                id
                commentCount
                topLevelCommentCount
            }
            ugcArticleOfficialSolutionArticle(questionSlug: $titleSlug) {
                uuid
                chargeType
                canSee
                hasVideoArticle
            }
            question(titleSlug: $titleSlug) {
                title
                titleSlug
                questionId
                questionFrontendId
                questionTitle
                translatedTitle
                content
                translatedContent
                categoryTitle
                difficulty
                stats
                companyTagStatsV2
                topicTags {
                    name
                    slug
                    translatedName
                }
                positionLevelTags {
                    name
                    nameTranslated
                    slug
                }
                similarQuestionList {
                    difficulty
                    titleSlug
                    title
                    translatedTitle
                    isPaidOnly
                }
                mysqlSchemas
                dataSchemas
                frontendPreviews
                likes
                dislikes
                isPaidOnly
                status
                canSeeQuestion
                enableTestMode
                metaData
                enableRunCode
                enableSubmit
                enableDebugger
                envInfo
                isLiked
                nextChallenges {
                    difficulty
                    title
                    titleSlug
                    questionFrontendId
                }
                libraryUrl
                adminUrl
                hints
                codeSnippets {
                    code
                    lang
                    langSlug
                }
                exampleTestcaseList
                hasFrontendPreview
                featuredContests {
                    titleSlug
                    title
                }
            }
        }
    """
    variables = {"titleSlug": titleSlug}
    return leetcode_query(query, variables)

def problemsetPanelQuestionList(searchKeyword, variables=None):
    query = """
        query problemsetPanelQuestionList($filters: QuestionFilterInput, $searchKeyword: String, $sortBy: QuestionSortByInput, $categorySlug: String, $limit: Int, $skip: Int) {
            problemsetPanelQuestionList(
                filters: $filters
                searchKeyword: $searchKeyword
                sortBy: $sortBy
                categorySlug: $categorySlug
                limit: $limit
                skip: $skip
            ) {
                questions {
                    id
                    titleSlug
                    title
                    translatedTitle
                    questionFrontendId
                    paidOnly
                    difficulty
                    topicTags {
                        name
                        slug
                        nameTranslated
                    }
                    status
                    isInMyFavorites
                    frequency
                    acRate
                }
                totalLength
                finishedLength
                panelName
                hasMore
            }
        }
    """
    variables = variables or {}
    variables["searchKeyword"] = searchKeyword
    return leetcode_query(query, variables)

def ugcArticleOfficialSolutionArticle(questionSlug):
    query = """
        query ugcArticleOfficialSolutionArticle($questionSlug: String!) {
            ugcArticleOfficialSolutionArticle(questionSlug: $questionSlug) {
                ...ugcSolutionArticleFragment
                content
                isSerialized
                isAuthorArticleReviewer
                scoreInfo {
                    scoreCoefficient
                }
            }
        }
        fragment ugcSolutionArticleFragment on SolutionArticleNode {
            uuid
            title
            slug
            summary
            author {
                realName
                userAvatar
                userSlug
                userName
                nameColor
                certificationLevel
                activeBadge {
                    icon
                    displayName
                }
            }
            articleType
            thumbnail
            summary
            createdAt
            updatedAt
            status
            isLeetcode
            canSee
            canEdit
            isMyFavorite
            chargeType
            myReactionType
            topicId
            hitCount
            hasVideoArticle
            reactions {
                count
                reactionType
            }
            title
            slug
            tags {
                name
                slug
                tagType
            }
            topic {
                id
                topLevelCommentCount
            }
        }
    """
    variables = {"questionSlug": questionSlug}
    return leetcode_query(query, variables)

def randomQuestionV2():
    query = """
        query randomQuestionV2($favoriteSlug: String, $categorySlug: String, $searchKeyword: String, $filtersV2: QuestionFilterInput) {
            randomQuestionV2(
                favoriteSlug: $favoriteSlug
                categorySlug: $categorySlug
                filtersV2: $filtersV2
                searchKeyword: $searchKeyword
            ) {
                titleSlug
            }
        }
    """
    return leetcode_query(query)
