# Neutron Story Progression

Neutron story progression is intended to be an open source story progression and world control mod for The Sims 4. It aims to be organic and have sensible defaults, and address issues that current story progression mods have. The most important thing is that **"story progression" should be based on actual story instead of random checks and instant marriage.**

## Design

Neutron will be design for true story progression, in multiple areas of NPC Sims' lives. These areas, primarily, are:

* Friendships
* Clubs
* Romance & Family
* Moving
* Careers, Fame, & University
* Skills & Aspirations

There aren't any promises, but there are a few issues I have with how EA handles these aspects and I don't feel they are adequately addressed by other story progression mods.

### Issues

To start, the core issue with how The Sims 4 handles NPCs is that they do not exist when they aren't observed. This creates a very artificial setting, where nothing happens unless the player specifically wants it to happen. The most offensive example, in my opinion, is NPC children. Say you have a branch of a family line you don't play. You might set them up to be married and have a child, but once the child is there, the child does nothing. As a toddler they will learn nothing, and as a child they complete no aspirations and gain no skills. As an adult, they will be jobless. Unless directly controlled, any NPC will do absolutely nothing with their life. This is how sims controlled by you always end up marrying sims without the most basic of skills. This is also the reason neighborhoods die and are replaced by randomly generated townies.

In gameplay, NPCs revolving around the player shatters the illusion of a simulated world. Crafting an intricate system to make the player think that NPCs have real lives outside of their view will make gameplay more enjoyable, and the characters they interact with more diverse.

### Systems

**Friendships** and who NPCs know should be central to how story progression works. NPCs should start and build friendships on their own, under a few key criteria:

* Friendships are more likely to start between sims with compatible traits.
* Friendships are develop better based on traits and mutual friendships.
* Friendships are more likely to develop between adult sims of the same "status", e.g. two famous sims.

Sims may also lose friendships, with a few rules:

* Incompatible traits can cause sims to lose friendships.
* Certain traits, like Erratic, Evil, and Mean may make it harder to gain and maintain friendships.
* If a sim with the "Hates Children" trait may lose friendship with their children, or children of partners and friends. This in turn may cause them to lose friendship with said partners and friends.

**Friendships** should also effect **Clubs**:

* A sim might join a club if an NPC they are friends with is a part of it and they meet criteria.
* NPCs will also join clubs if they meet criteria and a number of club activities align with their traits.

Sims will automatically be removed from clubs when they no longer meet the criteria, and club leaders will be replaced.

The most important system **Friendships** will effect is **Romance & Family**. The rules for initiating **Romance** would be as follows:

* Romance is more likely to start with sims that have an existing positive friendship.
* Romance very rarely happens instantly. Perhaps two "Romantic" sims may get quickly married, but otherwise there's a progression between significant other, engaged, and married.
* Young Adults are far less likely to get married, but may start and break off relationships. Teens will never get married but may also start relationships between each other. Chances will be configurable for all eligible ages.
* Relationships are trait-based, with compatibility being scored based on how many incompatible traits, with there being a global "tolerance" setting.
* YAs and teens may start relationships with incompatible sims, if enabled.
* Un-flirty sims are far less likely to start relationships than other sims, while Romantic sims may be more likely.
* Sims in a committed relationship with played sims should not develop external romantic relationships.
* Homeless sims may only start romance with other homeless sims, by default
* Butlers cannot start external relationships

Like friendships, romantic relationships can break down:

* If a pregnancy occurs with a sim who Hates Children or is Non-Committal, it can harm the romantic relationship between parents.
* If a relationship was started between two incompatible sims, there's a chance of breakup.
* Mean, Evil, Jealous, and Non-Committal sims may harm their relationships.
* If an affair occurs, it will cause large relationship loss. Double so if the victim is Jealous or Family-Oriented.
* Divorce and breakups can occur if the relationship dips too far.
* There'll also be a (adjustable) chance that sims in the significant other stage break without relationship loss.
* If a sim gets too low of a relationship with a child of their partner, a breakup may occur.

Regarding affairs:

* They do not always cause pregnancy.
* They may happen between two sims that know each other and have high friendship, and potentially previous romantic relationship.

**Family** needs to grow organically out of **Romance** and **Friendship**. The rules for how families form would be as follows:

* Sims should only begin pregnancies with sims they have a pre-existing relationship with.
* Young Adults should very rarely start pregnancies. Situations where it's acceptable are:
  * They are married.
  * A small (by default) chance roll for pregnancy occurs between them and an unmarried partner. This chance will be modified by traits.
    * In the case that a pregnancy occurs between unmarried partners, they are likely to marry unless there are trait conflicts or the pregnancy causes relationship loss according to traits.
* Adults may also have a small chance of pregnancy between them and an unmarried partner, modified by traits.
  * Rules for auto-marriage will be the same as those for YAs.
* Unless same-sex pregnancy is enabled, sims in same-sex relationships will choose to adopt instead. The adopted child will take on the last name of the parents.
* By default, Adults will only have children if both parents will not die before the child becomes a Teen.
* Homeless sims may only start families with other homeless sims, by default.
* NPC Roommates and butlers cannot start families.

* An unmarried sim far along enough into adulthood may choose to adopt.

The traits and relationships of the family members should affect the progression of the children to adulthood:

* Optionally, NPCs will try to inherit personality traits from family members instead of generating a personality trait on age up.
* Sims with traits like Irresponsible, Hates Children, and Lazy are less likely to teach their toddlers and children different skills.
* Conversely, sims with traits like Responsible, Family Oriented, and Good are more likely to teach their toddlers and children.
* Sims with good and bad character value traits will influence the character values of their children over time.
* All of the above will effect how the child progresses through grade school

**Moving** is tied closely to family:

* Ideally, if a couple wants a child they will try to move to a lot with enough beds for a child. Implementation wise this may be difficult/hacky
* Single sims, unless their household is marked as ancestral, may move out as they age up to YA.
  * If the household is marked as ancestral, they will only move if they have a younger sibling
* Moving will happen for marriages based on household space and who has dependents.

* Moving for breakups will be based on who has the best relationship with dependents.

Additional goals for moving, unrelated to family are:

* Sims should not necessarily move from group homes - for example, a group of roommates should not split because they were all single.

* The option to prevent homeless sims from moving in should be available.
* The option to prevent only game-generated homeless sims from moving in. This will allow Neutron to handle cases like breakups or sims moving out of dorms.

**Careers**, **University**, & **Fame** are the next set of systems Neutron should expand on. To start, when an NPC reaches YA, they should decide on whether or not they will go to college. There will be an adjustable base chance, but if the parents have a degree a sim will be more likely to pursue a degree. If a sim chooses not to pursue a degree:

* They will pick a career to start off with at a base level, determined by their high school grades.
* If they have a good relationship with their parents, they may go into the same career as a parent.

If picked for a degree, there's a global limit on dorm residents (likely 3 by default, to match with EA's defaults). If that limit isn't met, a single YA without dependents will be moved into an available University Housing lot. Otherwise if they aren't famous or in an ancestral household:

* If enabled, single YAs without dependents will be moved into homeless, single-sim households and marked as available to be roommates, as opposed to the randomly generated roommates. This setting will be disabled by default.
  * If the game can't properly pick sims automatically, we might want to recommend the "Choose Your Roommates" mod by LittleMsSam as an alternative

* If disabled, NPC students will stay in their existing homes.
* All sims, including those moved to a university lot, will try to move back in with existing family once graduated or after failing, starting with parents. If that fails, they'll be marked for regular move-in procedures.

EA's story progression should handle getting them through college.

For Fame, Sims will have a chance to become famous and progress in fame level based on various factors:

* If a sim is already famous, they have a chance to progress in fame level based on a random check

* If a sim isn't famous, they can become so through different factors:
  * Friendships and feuds with famous sims
  * Being the child of a famous sim
  * There's a small base chance for a random sim to become famous.

This is all to help prevent all famous sims from dying out.

Once graduated or after failing, these sims will try to move into homes of existing family members starting with parents. Otherwise they'll be marked for regular move-in procedures.

**Skill Progression** and **Aspirations** might be one of the more difficult forms to implement. Some ideas for how it might work:

* As mentioned above, the progression of toddlers and children will be dependent on the traits of their parents
* For children, a supportive family means they may be able to successfully roll for completion of one of the child roles and aspirations

* For Teens-Adults, there are various "basic" skills like Cooking and Handiness that all NPCs should roll to learn up to level 2-3. Skill progression past those is based on traits and aspirations.
* As an example:
  * Sims with "Mental" traits and aspirations will choose to develop "Mental" skills like Handiness, Logic, Programming, and Video Gaming. This includes traits like "Mentally Gifted" earned by completing child aspirations

### Miscellaneous Goals To Keep In Mind

* It should take at least 3 days for a relationship to progress from significant other to marriage on normal lifespan settings.
* The player should be aware of the actions of sims close to the active household by default.
* Disrupting player plans with instant action is discouraged.